# integrate_results.py
from query_enhancement import enhance_query
from article_retrieval import get_articles_and_images

def integrate_query_and_retrieval(user_query):
    original, enhanced = enhance_query(user_query)
    results = get_articles_and_images(enhanced)
    return original, enhanced, results

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    original, enhanced, articles = integrate_query_and_retrieval(user_query)
    print(f"Original Query: {original}")
    print(f"Enhanced Query: {enhanced}")
    for idx, article in enumerate(articles):
        print(f"Article {idx+1}: {article['title']}")
        print(f"Summary: {article['summary']}")
        print(f"Image URL: {article['image_url']}")
        print()
