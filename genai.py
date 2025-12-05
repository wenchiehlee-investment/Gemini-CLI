from google import genai

client = genai.Client(api_key="AIzaSyA-GZvh_EYBPb6A5970Ka4ypEfJsdkGzDc")

response = client.models.generate_content(
    model="gemini-2.5-pro", contents="Explain how AI works in a 100+ words in traditional chinese"
)
print(response.text)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="provide python code how to know the quota of google genai api"
)
print(response.text)