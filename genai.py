import os
from google import genai

# Retrieve API key from environment variable
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-pro", contents="Explain how AI works in a 100+ words in traditional chinese"
)
print(response.text)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="provide python code how to know the quota of google genai api"
)
print(response.text)