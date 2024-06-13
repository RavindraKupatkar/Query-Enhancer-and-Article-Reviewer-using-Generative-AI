# query_enhancement.py
import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def enhance_query(original_query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "I want you to act as a Expert in NEWS industry, who has knowledge of types of NEWS and current affairs."},
            {"role": "user", "content": f"I'm going to pass you sentence and you need to enhanced that sentence and give enhaced sentence as a output: {original_query}"}
        ]
    )
    enhanced_query = response['choices'][0]['message']['content'].strip()
    return original_query, enhanced_query
