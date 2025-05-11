# news_digest.py

import openai
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from news_parser import fetch_rss_feeds

# Load environment variables from .env file
load_dotenv()

# Set up API and email credentials from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Function to generate a news digest from RSS summaries using OpenAI
def generate_news_digest(rss_summary):
    print("Generating news digest from RSS summary...")
    prompt = f"""
You are my personal news assistant. Turn these headlines into a structured morning newsletter with the following sections:

GLOBAL HEADLINES
GEOPOLITICS (subsections for North America, Middle East, Asia-Pacific, Europe, Africa)
WORLD ECONOMY (subsections for Trade, Markets/Indicators, Policy)
COMPANIES

Format:
- Use the structure and subcategories above. If subsections don't make sense based on provided news, you may adjust those.
- Pick the most important 5 headlines to pull up in the Global Headlines sections. 
- Max 2 sentences per bullet.
- Always include a source link at the end of each summary, in form of a hyperlink with the label being the source name (e.g., WSJ)
- Prioritise WSJ (Wall Street Journal) as the first source link behind each summary, when available.
- Use only the rss-summary provided below as input for news.
- Refer to this example and follow its tone, style and structure (but ignore the actual news):

Example email here:

GLOBAL BRIEFING - THURSDAY 13TH FEBRUARY 2025

GLOBAL HEADLINES

● Trump and Putin agree to start Ukraine negotiations [All]; Hegseth rules out Ukraine’s NATO membership and US security guarantees [BBC, CBS, CNN, Washington Post, Politico, Financial Times, Economist].

● Egypt working on “comprehensive vision” for Gaza to counter Trump proposal, as mediators step up efforts to save ceasefire [BBC, Wall Street Journal, Fox, Guardian].

● Gabbard sworn in as US Director of National Intelligence [Washington Post, Bloomberg, New York Times, Wall Street Journal].

● US inflation rose to 3% in January, Trump repeats call for lower interest rates [New York Times, Wall Street Journal, Financial Times, Bloomberg, Reuters].

● Chevron to cut up to 20% of its workforce by next year [Financial Times, Bloomberg].


GEOPOLITICS


Ukraine/Russia

Trump and Putin agree to start Ukraine negotiations. All outlets, including CNN and Washington Post, cover President Trump saying he held a “lengthy and highly productive phone call” with President Putin and that they agreed to start negotiations “immediately”. Trump said he and Putin agreed “to work together, very closely”, including visits to each other’s nations, and could meet in Saudi Arabia in the “not too distant future”. The US negotiating team would include Secretary of State Rubio, CIA Director Ratcliffe, National Security Adviser Waltz and Middle East envoy Witkoff. There was no explanation from the White House why Ukraine envoy Kellogg was not on the list.

BBC reports Kremlin spokesman Peskov said Putin and Trump agreed “the time has come for our countries to work together”, but warned it was “essential to settle the reasons for the conflict”. Peskov said Putin invited Trump to Moscow and is prepared to meet with US officials to discuss “issues of mutual interest”. Guardian notes Trump said he was “ok” with Ukraine not joining NATO, adding it was “unlikely” Kyiv would reclaim much occupied land back from Russia. He insisted Zelensky would not be frozen out of negotiations but hinted that elections should soon take place as Zelensky’s “poll numbers aren’t particularly great”.

Trump later speaks to Zelensky. Wall Street Journal quotes President Zelensky saying the two discussed “the possibilities of achieving peace”. Bloomberg notes that earlier, Treasury Secretary Bessent told Zelensky in Kyiv that the US will continue to provide support for Ukraine in exchange for “an economic cooperation agreement”.

Speaking to Economist just before Trump’s announcement, Zelensky warned Russia could provide the US with “manipulative information” if Ukraine is excluded from negotiations. He conceded that NATO membership is unlikely, and suggested Ukraine must instead “double” the size of its army to match Russia’s.

Separately, US and Chinese sources told Wall Street Journal that Chinese officials have approached the Trump administration about hosting a Trump-Putin summit, without Zelensky’s involvement, and facilitating peacekeeping efforts after an eventual ceasefire. The White House declined to confirm whether it had received China’s offer, but still rejected it as “not viable”.

Europe demands role in negotiations. New York Times highlights a statement from France, Germany, the UK, Italy, Poland and Spain calling for Ukraine and Europe to be part of negotiations and for strong security guarantees for Kyiv.

Concerns the US and Russia will negotiate the future of the continent’s security over the heads of the Europeans is a trending theme in coverage. Politico says events left European diplomats “in shock” and unsure how to respond. Wall Street Journal and Guardian quote senior European officials saying Trump’s concessions surrendered leverage in upcoming talks. Financial Times notes the Kremlin’s readout of the call was more restrained than Trump’s and did not suggest Russia was prepared to soften its stance. Bloomberg says European officials were “stunned” by the Trump-Putin call, of which key allies were given no notice. An official said European fears centre around the fact no one in the Trump administration has any real experience of negotiating with the Russians. The outlet calculates that protecting Ukraine and expanding the EU’s militaries could cost an additional $3.1 trillion over the next decade.

Call ends Putin’s isolation from Western leaders. New York Times says the Trump-Putin call was a major milestone for the Russian leader that signalled the collapse of Western efforts to isolate him diplomatically. Washington Post comments that Putin achieved his goal of direct negotiations with Washington and managed to secure major concessions from Trump even before negotiations formally began.

Hegseth rules out Ukraine’s NATO membership and US security guarantees. BBC and CBS cover Defence Secretary Hegseth setting out the US position before the Trump-Putin call, saying a return to Ukraine’s pre-2014 borders and Ukraine’s NATO membership are “unrealistic” objectives. He ruled out a US or NATO role in security guarantees for Ukraine, saying these should involve “European and non-European troops” along with international oversight of the boundary between Russian and Ukrainian forces. CNN adds Hegseth said the US remained committed to NATO and did not indicate an imminent halt in US military aid for Ukraine. However, he called on Europe to take more responsibility for its security, warning border security issues and threats posed by China prevent the US from being “primarily focused on the security of Europe”.

The remarks are seen as the most direct outline yet of Trump’s Ukraine approach. Washington Post notes that while the comments were unlikely to catch European allies off guard, they still mark a significant departure from Biden administration policy. Financial Times cites senior Ukrainian officials saying they will work to find alternative security arrangements with European allies, while one Ukrainian official told Economist Kyiv believes the terms of peace “will all be decided without Ukraine”.


Middle East

Egypt working on “comprehensive vision” for Gaza to counter Trump. BBC cites the Egyptian Foreign Ministry saying it will work with the US "to achieve a comprehensive and just peace in the region” that does not require the displacement of Palestinians. Sources later told Wall Street Journal that Egypt is seeking funding sources in the region to help form a committee of technocrats in Gaza to administer the territory, while Palestinians trained by Arab forces provide security. The effort will reportedly seek to separate the issue of Palestinian statehood from Gaza’s reconstruction. According to Fox, Egyptian sources told Qatari media that the three to five-year plan would involve Arab countries, the EU and the UN, with no mention of the US or Israel. EU sources said they were not aware of the bloc’s involvement in the plan.

Egypt and Qatar step up efforts to save ceasefire. A senior Egyptian source told BBC that mediators are “intensifying their diplomatic efforts”, with a Hamas official confirming a senior delegation led by leader Khalil al-Hayya arrived in Cairo in a bid “to contain the current crisis”. Guardian quotes senior Hamas official Mahmoud Mardawi saying there are “positive signals” the hostage handover will go ahead as planned.

Israel considers strikes on Iranian nuclear sites. US officials told Wall Street Journal and Washington Post that US intelligence agencies concluded that Israel is considering taking advantage of Iran’s weakness with a strike on the Fordow and Natanz nuclear facilities in the first six months of this year, and may urge the Trump administration to back the strikes. A second report made the same assessment in the early days of Trump’s presidency.

North America

Gabbard sworn in as US Director of National Intelligence. Washington Post reports the Senate voted 52 to 48 in favour of Gabbard’s nomination, with Mitch McConnell the only Republican to cast his vote against her. Speaking alongside Trump at the White House, Bloomberg quotes Gabbard claiming the US intelligence community was at “an all-time low” due to “weaponisation and politicisation”. The Senate also advanced Robert Kennedy’s nomination in a procedural vote, with a final vote expected today.

New York Times comments that the vote demonstrates Trump’s political control over Republican lawmakers, as some cabinet members favour policies most of the party’s Senators oppose. Wall Street Journal’s editorial board continues to express concern that Gabbard could downplay security risks to avoid confronting adversaries and undermine Waltz’s more sound advice to Trump.

Trump closes federal worker buyout amid reports of mass firings. Washington Post and Bloomberg report a federal judge in Boston lifted a pause on the government’s deferred resignation programme, in a win for the Trump administration which later closed the programme saying 75,000 employees have accepted the deal. Comes amid reports from CNN that mass firings have begun at the Department of Education and the Small Business Administration.


Asia-Pacific

Trump to host Modi at White House today. Previews of the meeting focus on PM Modi’s overtures to Trump, with New York Times saying Indian companies are in talks to increase purchases of US energy supplies. The two leaders are also expected to discuss expanded spending on US defence equipment, while a source told Financial Times it is “quite clear” Trump expects India to buy more from the US, including oil. Wall Street Journal says Modi will be able to point to recent reductions in Indian tariffs on some US goods. Sources told Reuters that Modi is also set to meet Musk to discuss Starlink's entry in India.


Africa

Sudan agrees deal for Russian naval base. Financial Times notes FM Al-Sharif said on a visit to Moscow that Sudan has agreed a deal for Russia to establish a naval base on the Red Sea coast. The Kremlin did not comment, but if confirmed, the development would mark a rare success for Russia’s drive to expand its network of military bases in the region.


WORLD ECONOMY


Markets/Indicators

US inflation rose to 3% in January. New York Times and Wall Street Journal are among outlets to cover an unexpected acceleration of the consumer price index from last month to its fastest pace in almost a year and a half. There were sharp increases in prices across a range of categories such as groceries, gasoline, used cars and air fares. Financial Times says the reading bolsters the case for the Federal Reserve to proceed very slowly with any further interest rate cuts, with Bloomberg quoting Chair Powell telling the House Financial Services Committee that the central bank is "not quite there yet” on bringing inflation down to target.

Reuters notes that just ahead of the reading, Trump called for the Fed to reduce interest rates, claiming they would “go hand in hand” with tariffs. Wall Street Journal’s editorial board points out the contradiction in Trump’s repeated calls for looser monetary policy even as prices continue to rise, warning that renewed inflation from easier money and new tariffs is the biggest threat to the President’s approval rating.


COMPANIES

Chevron to cut up to 20% of its workforce by next year. Financial Times and Bloomberg highlight a statement from Chevron confirming its intention to let go of around 9,000 employees worldwide by 2026 in order to “simplify” its organisational structure and “position the company for stronger long-term competitiveness”.

Blue Origin preparing for large reduction to workforce. Sources told Bloomberg the company could let go of up to 1,000 employees as it shifts its focus from R&D towards accelerating the pace of rocket launches.

X agrees to pay $10 million to settle Trump lawsuit. Wall Street Journal reports X became the second social media platform to settle litigation that Trump filed when the companies deplatformed him over his role in the January 6 Capitol riot. Sources told the paper Trump’s legal team continued to pursue the lawsuit despite CEO Elon Musk’s proximity to the President and the fact that he spent $250 million to help elect him.



Text:
{rss_summary}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4.1-mini",
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

    # Retrieve variables. 
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    EMAIL_FROM = os.getenv("EMAIL_FROM")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    EMAIL_TO = os.getenv("EMAIL_TO")
    
    if not EMAIL_FROM or not SMTP_PASSWORD:
        raise ValueError("Missing email or password.")

    msg = EmailMessage()
    msg.set_content(body)
    msg["From"] = EMAIL_FROM 
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject

    try:
            # Establish connection to SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection using TLS
            server.login(EMAIL_FROM, SMTP_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully.")
        
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function to coordinate the workflow
# 1. Fetch RSS feeds and summarize
# 2. Generate a newsletter using OpenAI
# 3. Email the newsletter to the recipient

def main():
    print("Starting main process...")
    rss_summary = fetch_rss_feeds()
    print("RSS summary fetched.")
    newsletter = generate_news_digest(rss_summary)
    send_email("DAILY NEWS BRIEFING", newsletter)
    print("Process completed.")

if __name__ == "__main__":
    main()
