import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
ZENSERP_KEY = os.getenv("ZENSERP_KEY")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not ZENSERP_KEY:
    raise ValueError("ZENSERP_KEY not found in environment variables.")
if not GEMINI_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Configure Gemini client
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")


def fetch_trending_titles(topic, max_results=10):
    """Fetch trending YouTube video titles for a topic using Zenserp."""
    try:
        url = "https://app.zenserp.com/api/v2/search"
        params = {
            "apikey": ZENSERP_KEY,
            "q": topic,
            "tbm": "vid",
            "num": max_results
        }
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        results = resp.json().get("video_results", [])
        if not results:
            print("Warning: No video results found.")
        titles = [video.get("title") for video in results[:max_results] if "title" in video]
        return titles
    except Exception as e:
        print(f"Error fetching trending titles: {e}")
        return []


def gpt_content_research(topic, trending_titles):
    """Generate new ideas and analyze content gaps using Gemini."""
    try:
        prompt = (
            f"You are a YouTube content research agent.\n"
            f"Given the topic: '{topic}'\n"
            f"Trending video titles:\n" +
            "\n".join(f"- {t}" for t in trending_titles) +
            "\n\n1. Suggest 5 unique and clickable video title ideas for this topic.\n"
            "2. Analyze the above trending titles and list 3 content gaps (angles not covered).\n"
            "Return your answer as:\n"
            "Generated Ideas:\n1.\n2.\n3.\n4.\n5.\nContent Gaps:\n1.\n2.\n3."
        )
        response = model.generate_content(prompt)
        text = response.text
        # Parse output
        ideas = []
        gaps = []
        in_ideas = in_gaps = False
        for line in text.splitlines():
            if line.strip().startswith("Generated Ideas"):
                in_ideas, in_gaps = True, False
                continue
            if line.strip().startswith("Content Gaps"):
                in_ideas, in_gaps = False, True
                continue
            if in_ideas and line.strip().startswith(tuple("12345")):
                ideas.append(line.split(".", 1)[1].strip())
            if in_gaps and line.strip().startswith(tuple("123")):
                gaps.append(line.split(".", 1)[1].strip())
        return ideas, gaps
    except Exception as e:
        print(f"Error with Gemini: {e}")
        return [], []


def research_youtube_content(topic):
    """Main function to research YouTube content for a topic."""
    trending = fetch_trending_titles(topic)
    ideas, gaps = gpt_content_research(topic, trending)
    return {
        "Trending Titles": trending,
        "Generated Ideas": ideas,
        "Content Gaps": gaps
    }

# Example usage:
if __name__ == "__main__":
    user_topic = input("Enter a YouTube topic: ")
    result = research_youtube_content(user_topic)
    for key, value in result.items():
        print(f"\n{key}:")
        if not value:
            print("  (No data found)")
        for i, item in enumerate(value, 1):
            print(f"{i}. {item}")
