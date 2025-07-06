# YouTube Content Research AI Agent

This Python project uses AI to generate original YouTube video ideas and identify content gaps in trending videos.

It combines:
- Zenserp API to fetch real-time trending YouTube titles
- Google Gemini API to generate content ideas and analyze gaps

---

## Features

- Fetches trending YouTube video titles based on any topic
- Uses Gemini to generate 5 unique and clickable YouTube title ideas
- Identifies 3 content gaps that current creators are not covering
- Useful for content creators, marketers, and YouTube automation workflows

---

## Video Demo

Click the link below to preview how it works:

[Watch Demo](https://drive.google.com/file/d/1W0L0OzHph9IBHhVoZk_Phb0kcBcCH1HI/view?usp=drive_link)

---

## Screenshot

A preview of the tool running in the terminal:

![Terminal Output](demo/demo(2).png)

---

## How to Run

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/youtube-agent.git
cd youtube-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API keys

Create a `.env` file in the root folder:

```env
ZENSERP_KEY=your_zenserp_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Do not upload your `.env` file to GitHub. Instead, include a `.env.example` file with placeholders.

### 4. Run the tool

```bash
py main.py
```

When prompted, enter a topic (e.g., `ai tools for productivity`).

---

## Project Structure

```
youtube-agent/
├── main.py
├── README.md
├── .env.example
├── requirements.txt
├── demo/
│   ├── demovideo.mp4
│   └── demo(2).png
```

---

## Sample Output

```bash
Enter a YouTube topic: best selling ai
```

### Trending Titles:
1. How to create best selling designs with AI  
2. The BEST AI Digital Products to Sell Online ($10k/Month+)

### Generated Ideas:
1. AI That SELLS: The Ultimate Guide to Profitable AI Products (2024)  
2. From Zero to Hero: Building an AI-Powered Business (Case Studies!)  

### Content Gaps:
1. Ethical concerns of selling AI  
2. Selling B2B AI services  
3. Using AI to research best-selling product ideas  

---

## License

This project is open-source under the MIT License.
