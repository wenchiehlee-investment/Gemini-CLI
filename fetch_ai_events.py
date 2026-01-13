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

    print("Fetching major AI events (History to Present)...")

    prompt = """
    You are a Technology Historian specializing in Artificial Intelligence.
    
    Task: Search for and extract a list of the TOP 50-100 CRITICAL events in the history of Artificial Intelligence, with a heavy focus on the modern "Deep Learning" and "Generative AI" eras (2010-Present), but also including foundational milestones.
    
    Focus on these specific Categories (類別) and Sub-categories (子類別):
    
    1. 技術突破 (Technological Breakthrough):
       - 演算法創新 (Algorithm) - e.g., Transformer Paper (Attention Is All You Need), AlphaGo, AlexNet.
       - 模型架構 (Model Architecture) - e.g., BERT, GANs, Diffusion Models.
    
    2. 產品發布 (Product Launch):
       - 生成式AI (Generative AI) - e.g., ChatGPT, GPT-4, Claude, Gemini, Midjourney, Stable Diffusion.
       - 語音與助理 (Voice & Assistants) - e.g., Siri, Alexa (early days).
       - 硬體晶片 (Hardware) - e.g., NVIDIA H100, Google TPU launch.
    
    3. 產業動態 (Industry Dynamics):
       - 企業併購與投資 (M&A & Investment) - e.g., Microsoft invests in OpenAI, Google acquires DeepMind.
       - 公司人事 (Corporate Events) - e.g., Sam Altman firing/rehiring, founding of OpenAI.
       - 市值里程碑 (Market Cap) - e.g., NVIDIA becomes most valuable company.
    
    4. 政策與倫理 (Policy & Ethics):
       - 監管法規 (Regulation) - e.g., EU AI Act, US Executive Order on AI.
       - 安全與爭議 (Safety & Controversy) - e.g., Deepfake scandals, AI Safety Summit.
    
    Output Format:
    Produce a valid CSV file content with the following headers:
    "類別", "子類別", "事件名稱", "開始日期", "結束日期", "備註", "Link1", "Link2"
    
    Requirements:
    - Language: All text must be in Traditional Chinese (繁體中文).
    - Dates: Format YYYY-MM-DD. For research papers, use the publication date.
    - "備註" (Note): Briefly explain the significance (e.g., "開啟了生成式AI熱潮").
    - "Link1": MANDATORY. Provide a reliable source URL (arXiv, TechCrunch, Official Blog, News).
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
