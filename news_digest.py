# news_digest.py

import openai
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from news_parser import fetch_and_summarize_rss

# Load environment variables from .env file
load_dotenv()

# Set up API and email credentials from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Function to generate a news digest from RSS summaries using OpenAI
def generate_news_digest(rss_summary):
    print("Generating news digest from RSS summary...")
    prompt = f"""
You are my personal news assistant. Turn these headlines into a structured morning newsletter with the following sections:

GLOBAL HEADLINES
GEOPOLITICS (North America, Middle East, Asia-Pacific, Europe, Africa)
WORLD ECONOMY (Trade, Markets/Indicators, Policy)
COMPANIES

Format:
- Use the structure and subcategories above.
- Max 2 sentences per bullet.
- Always include a source link at the end of each summary.
- Prioritise WSJ (Wall Street Journal) as the first source when available.
- Use only these sources when possible: Wall Street Journal, AP, Politico, Reuters, Financial Times, New York Times, BBC, AFP, Bloomberg, Economist, CNN, Handelsblatt, Washington Post.
- Refer to this example and follow its tone, style and structure:

[Insert example email here – the one you previously provided]

Text:
{rss_summary}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a world-class news summarizer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )

    print("News digest generated successfully.")
    return response.choices[0].message.content

# Function to send the news digest as an email
def send_email(subject, body):
    print("Preparing to send email...")
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
    print("Email sent successfully.")

# Main function to coordinate the workflow
# 1. Fetch RSS feeds and summarize
# 2. Generate a newsletter using OpenAI
# 3. Email the newsletter to the recipient

def main():
    print("Starting main process...")
    rss_summary = fetch_and_summarize_rss()
    print("RSS summary fetched.")
    newsletter = generate_news_digest(rss_summary)
    send_email("GLOBAL BRIEFING", newsletter)
    print("Process completed.")

if __name__ == "__main__":
    main()
