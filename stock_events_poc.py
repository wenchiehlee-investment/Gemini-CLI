import os
import argparse
import datetime
from datetime import timedelta
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def update_readme(content, start_marker, end_marker):
    """Updates the README.md file between specific markers."""
    readme_path = "README.md"
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()
        
        start_pos = readme_content.find(start_marker)
        end_pos = readme_content.find(end_marker)
        
        if start_pos == -1 or end_pos == -1:
            print(f"Warning: Markers {start_marker} and {end_marker} not found in {readme_path}")
            return

        # Generate timestamp
        now = datetime.datetime.now()
        timestamp_str = now.strftime("產生時間: %Y-%m-%d %H:%M:%S") + " CST"


        new_content = (
            readme_content[:start_pos + len(start_marker)]
            + f"\n{timestamp_str}\n\n```csv\n" + content + "\n```\n" # Add timestamp here, use ```csv
            + readme_content[end_pos:]
        )
        
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Successfully updated {readme_path}")
        
    except Exception as e:
        print(f"Error updating README: {e}")

def generate_market_csv(update_readme_flag=False):
    # 1. Initialize Client
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.")
        return

    client = genai.Client(api_key=api_key)

    # 2. Calculate Date Range (Dynamic)
    today = datetime.date.today()
    # Define "Last Week" to "Next Week" as a sliding window: -7 days to +7 days
    start_date = today - timedelta(days=7)
    end_date = today + timedelta(days=7)
    
    date_range_str = f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
    print(f"Generating market events for period: {date_range_str}...")

    # 3. Construct Prompt
    # We explicitly ask for CSV format, define the columns, and request search grounding.
    prompt = f"""
    You are a financial data analyst.
    
    Task: Search for and extract scheduled stock market events for the period: {date_range_str}.
    
    Focus on identifying specific events including:
    1. Taiwan Stock Exchange (TWSE) and Taipei Exchange (TPEx) official schedules (holidays, open tenders).
    2. Key TWSE/TPEx listed company events: Earnings calls (法說會), Ex-dividend dates (除權息), Capital reductions, Shareholder meetings.
    3. Major Global Economic Data impacting Taiwan: US FOMC meetings, US CPI/PPI releases, Non-farm payrolls.
    4. Major Tech Earnings (e.g., TSMC, Apple, NVIDIA) if occurring in this range.

    Use Google Search to find real, specific dates and details.
    
    Output Format:
    Produce a valid CSV file content with the following headers:
    "類別", "子類別", "事件名稱", "開始日期", "結束日期", "備註", "Link1", "Link2"
    
    Columns Guidelines:
    - "類別" (Category): e.g., 公司行動, 經濟數據, 市場機制.
    - "子類別" (Sub-category): e.g., 法說會, 除權息, 財報發布, 利率決策.
    - "Link1", "Link2": specific source URLs found during your search verifying the event.
    
    Rules:
    - Dates must be in YYYY-MM-DD format.
    - Do not include markdown code block markers (like ```csv). Just the raw CSV text.
    - Ensure chinese characters are traditional chinese (繁體中文).
    """

    print("Sending request to Gemini 2.5 Flash with Google Search...")
    
    try:
        # Enable Google Search Tool
        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                response_modalities=["TEXT"]
            )
        )
        
        csv_content = response.text.strip()
        
        # Clean up if the model added markdown blocks despite instructions
        if csv_content.startswith("```"):
            csv_content = csv_content.strip("`").replace("csv\n", "", 1)

        # 4. Save to File
        output_file = "market_events.csv"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(csv_content)
            
        print(f"Successfully generated '{output_file}'.")
        print("-" * 30)
        print(csv_content)
        print("-" * 30)

        if update_readme_flag:
            update_readme(csv_content, "<!-- START_EVENTS_OUTPUT -->", "<!-- END_EVENTS_OUTPUT -->")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract Market Events")
    parser.add_argument("--update-readme", action="store_true", help="Update the README.md file with the output")
    args = parser.parse_args()
    
    generate_market_csv(args.update_readme)