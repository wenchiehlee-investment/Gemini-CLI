import os
import csv
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_historical_crashes():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.")
        return

    client = genai.Client(api_key=api_key)

    print("Fetching historical market crash events (1990-Present)...")

    prompt = """
    You are a financial historian.
    
    Task: Search for and extract a list of the TOP 100 CRITICAL historical events from 1990 to the present that caused significant stock market drops (crashes, corrections, or bear markets) in either the Global (US) or Taiwan markets.
    
    Focus on these specific Categories (類別) and Sub-categories (子類別):
    
    1. 金融危機 (Financial Crisis):
       - 亞洲金融風暴 (Asian Financial Crisis)
       - 網路泡沫 (Dot-com Bubble)
       - 次貸危機 (Subprime Crisis / Global Financial Crisis)
       - 歐債危機 (European Debt Crisis)
       - 銀行倒閉 (Bank Failure)
    
    2. 公共衛生 (Public Health):
       - 傳染病爆發 (Pandemic) - e.g., SARS, COVID-19
    
    3. 地緣政治 (Geopolitics):
       - 恐怖攻擊 (Terrorist Attack) - e.g., 911
       - 戰爭衝突 (War & Conflict) - e.g., Persian Gulf War, Russia-Ukraine
       - 貿易戰 (Trade War)
       - 政治黑天鵝 (Political Black Swan) - e.g., Brexit, 1996 Taiwan Strait Crisis (台海飛彈危機)
    
    4. 自然災害 (Natural Disaster):
       - 重大震災 (Major Earthquake) - e.g., 921 Earthquake, 311 Japan Earthquake
    
    5. 政策衝擊 (Policy Shock):
       - 貨幣政策 (Monetary Policy) - e.g., Aggressive Rate Hikes
       - 證所稅事件 (Stock Transaction Tax) - Specific to Taiwan (1990)
    
    Output Format:
    Produce a valid CSV file content with the following headers:
    "類別", "子類別", "事件名稱", "開始日期", "結束日期", "備註", "Link1", "Link2"
    
    Requirements:
    - Language: All text must be in Traditional Chinese (繁體中文).
    - Dates: Format YYYY-MM-DD.
    - "備註" (Note): Briefly explain the impact (e.g., "跌幅達...").
    - "Link1": MANDATORY. Provide a reliable source URL.
    - Quantity & Distribution: Find roughly 40 events in total, distributed as follows:
        * 1990-1999: ~10 events
        * 2000-2009: ~10 events
        * 2010-2019: ~10 events
        * 2020-Present: ~10 events
    - Do not include markdown code block markers.
    """

    print("Sending request to Gemini 2.5 Flash...")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                response_modalities=["TEXT"]
            )
        )
        
        csv_content = response.text.strip()
        
        # Clean up markdown
        if csv_content.startswith("```"):
            csv_content = csv_content.strip("`").replace("csv\n", "", 1)

        output_file = "historical_crashes-gemini3.csv"
        
        with open(output_file, "w", encoding="utf-8-sig", newline="") as f:
            f.write(csv_content)
            
        print(f"Successfully generated '{output_file}'.")
        print("-" * 30)
        print(csv_content)
        print("-" * 30)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_historical_crashes()
