import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_ai_events():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.")
        return

    client = genai.Client(api_key=api_key)

    print("Fetching major AI events (Market & Business Impact)...")

    prompt = """
    You are a Financial Technology Analyst.
    
    Task: Search for and extract a list of the TOP 50-100 CRITICAL Artificial Intelligence events that significantly impacted the **Stock Market, Corporate Valuations, or the Business Landscape**.
    
    Focus on events that:
    1. Caused noticeable stock price movements (e.g., NVIDIA, Microsoft, Google, TSM).
    2. Triggered major M&A (Mergers & Acquisitions) or huge Venture Capital investments.
    3. Launched products that disrupted industries or created new revenue streams.
    4. Influenced market sentiment or regulatory environments affecting business operations (e.g., Chip bans).

    Focus on these specific Categories (類別) and Sub-categories (子類別):
    
    1. 市場與資本 (Market & Capital):
       - 市值里程碑 (Market Cap Milestones) - e.g., NVIDIA hits $3T, Microsoft overtakes Apple due to AI.
       - 併購與投資 (M&A & Investment) - e.g., Microsoft invests $10B in OpenAI, Google buys DeepMind.
       - 股價波動 (Stock Movement) - e.g., Super Micro Computer surge, Chegg crash due to ChatGPT.

    2. 產品發布與商業化 (Product & Commercialization):
       - 生成式AI應用 (Generative AI Apps) - e.g., ChatGPT launch (sparked AI arms race), Copilot launch.
       - 企業級解決方案 (Enterprise Solutions) - e.g., Salesforce AI integration.
       - 硬體與基礎設施 (Hardware & Infra) - e.g., H100 announcement (AI gold rush), AMD MI300.

    3. 技術突破與轉折點 (Tech Breakthroughs as Market Catalysts):
       - 關鍵論文 (Seminal Papers) - e.g., "Attention Is All You Need" (foundation of modern value creation).
       - 模型發布 (Model Releases) - e.g., GPT-4 (set new industry standard).

    4. 政策與監管衝擊 (Regulation & Policy Impact):
       - 貿易限制 (Trade Restrictions) - e.g., US bans AI chip exports to China (impacted NVIDIA/AMD stocks).
       - 監管審查 (Regulation Scrutiny) - e.g., Antitrust investigations into AI partnerships.
    
    Output Format:
    Produce a valid CSV file content with the following headers:
    "類別", "子類別", "事件名稱", "開始日期", "結束日期", "備註", "Link1", "Link2"
    
    Requirements:
    - Language: All text must be in Traditional Chinese (繁體中文).
    - Dates: Format YYYY-MM-DD.
    - "備註" (Note): **Crucial**: Explain the *Business/Market Impact* (e.g., "NVIDIA股價當日上漲24%", "微軟市值超越蘋果", "引發AI軍備競賽").
    - "Link1": MANDATORY. Provide a reliable source URL (Bloomberg, CNBC, Reuters, TechCrunch).
    - Quantity: Aim for ~40-50 distinct high-impact events.
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

        output_file = "AI-event-gemini3.csv"
        
        with open(output_file, "w", encoding="utf-8-sig", newline="") as f:
            f.write(csv_content)
            
        print(f"Successfully generated '{output_file}'.")
        print("-" * 30)
        print(csv_content[:500] + "...\n(truncated for display)")
        print("-" * 30)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_ai_events()
