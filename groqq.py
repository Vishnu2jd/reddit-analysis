import json
import os
from groq import Groq

# Set up the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Function to classify a post using Groq's API
def classify_post(post):
    prompt = (
        "Classify the following post into only one of these categories:\n"
        "1. Engineering (e.g., software development, building something)\n"
        "2. Jobs situation (e.g., layoffs, placements, job market)\n"
        "3. Money (e.g., salary, compensation, cost of living)\n"
        "4. Office politics\n"
        "5. News\n"
        "6. Misc (if it doesn't fit into any other categories)\n"
        "7. Not enough context (if the provided information is insufficient for classification)\n\n"
        "The classification should reflect the main topic discussed in the post and I don't need any explanation. Just give me category number and nothing else so that it will be easier for for further study.\n\n"
        f"Title: {post['Title']}\n\n"
        f"Body: {post['Body']}\n\n"
        "Category:"
    )
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama3-70b-8192"
    )
    return response.choices[0].message.content.strip()

# Load posts from JSON file
with open('posts.json', 'r') as f:
    posts = json.load(f)

# Classify each post and store results
results = []
for post in posts:
    category = classify_post(post)
    post['Category'] = category
    results.append(post)

# Write results to a new JSON file
with open('classified_posts.json', 'w') as f:
    json.dump(results, f, indent=4)
