import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    print("Listing available Gemini models...\n")
    models = genai.list_models()
    for m in models:
        print(f"- {m.name}")
except Exception as e:
    print("❌ Failed to list models. Error:", e)
