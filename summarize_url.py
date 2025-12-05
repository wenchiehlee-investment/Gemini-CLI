import requests
import os
from bs4 import BeautifulSoup
from google import genai

# 1. Fetch Content
url = "https://murmurcats.com/margin-balance-market-guide/"
print(f"Fetching content from: {url}...")

try:
    # Add headers to mimic a browser (often needed for scraping)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract text (simple extraction)
    # Remove script and style elements
    for script in soup(["script", "style", "header", "footer", "nav"]):
        script.extract()
        
    text_content = soup.get_text(separator="\n")
    
    # Clean up whitespace
    lines = (line.strip() for line in text_content.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    clean_text = '\n'.join(chunk for chunk in chunks if chunk)
    
    print(f"Extracted {len(clean_text)} characters.")

except Exception as e:
    print(f"Error fetching URL: {e}")
    exit(1)

# 2. Summarize with Gemini
print("Summarizing with Gemini 2.5 Pro...")

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY environment variable not set")
    exit(1)

client = genai.Client(api_key=api_key)

try:
    # Using gemini-2.5-pro for its large context window and reasoning capabilities
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=f"請用繁體中文提供以下文章的詳細摘要。請重點關注融資餘額和市場相關性方面的關鍵點：\n\n{clean_text[:50000]}" # Limit to 50k chars just in case, though pro handles more
    )
    
    print("\n--- Summary ---\n")
    print(response.text)

except Exception as e:
    print(f"Error generating summary: {e}")
