from dotenv import load_dotenv
import os

load_dotenv()

print("ZENSERP_KEY:", os.getenv("ZENSERP_KEY"))
print("GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))
