import os
from google import genai

# Mock Data: In a real production app, this would be fetched via `requests` from a news API or website.
# We are simulating a "raw feed" of unstructured market text.
RAW_MARKET_DATA = """
MARKET INTELLIGENCE REPORT - DECEMBER 2025

[Week of Dec 1 - Dec 7, 2025]
- The Taiwan Stock Exchange (TWSE) operated normally.
- Dec 3: Taipei Exchange (TPEx) held an "Open Tender" event for government bonds.
- Dec 5: FTSE announced weight adjustments for component stocks after market close. This is a major liquidity event. Effective after market close on the 3rd Friday.
- Throughout the week: "Investor Conferences by TWSE Listed Companies" continued at the IT Center.

[Week of Dec 8 - Dec 14, 2025]
- Dec 8 (Mon):
    - Company Presentations (法說會): 勤益控 (1437), 鴻海 (2317), 致茂 (2360), 聯亞 (3081), 日電貿 (3090).
    - Trading Suspensions: 期街口布蘭特正2 (00715L), 斐成 (3313).
    - Stock Resumption: 瀚荃 (8103) resumes trading following capital reduction.
    - Short Selling Suspended: TSMC (2330), 00940.
- Dec 9 (Tue):
    - Ex-Dividend/Right (除權息): 華建 (2530), 宏正 (6277).
    - Company Presentations: TECO (1504), Lite-On (2301), Foxconn (2317), Compal (2324), Quanta (2382).
    - Shareholder Meeting: 麗升能源 (8087).
    - Economic Data: Foreign Exchange Reserves (Nov) release.
- Dec 11 (Thu):
    - Global: US FOMC Interest Rate Decision (approx 02:00 Taipei time). High impact on TAIEX opening.
    - Earnings: Broadcom, Oracle reports expected.
- Dec 12 (Fri):
    - Weekly market close.
"""

import argparse

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

        new_content = (
            readme_content[:start_pos + len(start_marker)]
            + "\n```csv\n" + content + "\n```\n"
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

    # 2. Construct Prompt
    # We explicitly ask for CSV format and define the columns.
    prompt = f"""
    You are a financial data analyst.
    Analyze the following unstructured market intelligence text.
    
    Task: Extract scheduled stock market events for "Last Week" (Dec 1-7, 2025) and "Next Week" (Dec 8-14, 2025).
    
    Output Format:
    Produce a valid CSV file content with the following headers:
    "類別", "子類別", "事件名稱", "開始日期", "結束日期", "備註"
    
    Rules:
    - Dates should be in YYYY-MM-DD format.
    - Category examples: "公司行動", "經濟數據", "市場機制", "全球事件".
    - Sub-category examples: "財報發布", "股息/權利", "暫停交易", "利率決策".
    - If an event happens on a single day, Start date and End date are the same.
    - Do not include markdown code block markers (like ```csv). Just the raw CSV text.
    
    Input Text:
    {RAW_MARKET_DATA}
    """

    print("Sending data to Gemini 2.5 Flash for extraction...")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        csv_content = response.text.strip()
        
        # Clean up if the model added markdown blocks despite instructions
        if csv_content.startswith("```"):
            csv_content = csv_content.strip("`").replace("csv\n", "", 1)

        # 3. Save to File
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
