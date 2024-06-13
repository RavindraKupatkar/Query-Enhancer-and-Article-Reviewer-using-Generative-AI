import requests
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_articles_and_images(query):
    
    url = "https://newsapi.org/v2/everything?qInTitle=business&apiKey=apikey"
   
       # params = {
    #     "q": query,
    #     # "apiKey": apikey,
    #     "language": "en",
    #     "pageSize": 10,  # Retrieve top 10 articles
    # }

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        search_results = response.json()

        articles = []
        for article in search_results.get("articles", []):
            articles.append({
                "title": article["title"],
                "summary": article["description"],
                "image_url": article.get("urlToImage"),
                "url": article["url"]
            })

        return articles
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        logger.error(f"JSON decode error: {json_err}")
        logger.debug(f"Response content: {response.text}")

    return []  # Return an empty list if there was an error
