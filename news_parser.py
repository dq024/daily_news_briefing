import feedparser

# Define the list of RSS feed URLs
RSS_FEEDS = [
    # The Wall Street Journal
    "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
    "https://feeds.a.dj.com/rss/RSSUSNews.xml",
    "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml",
    "https://feeds.a.dj.com/rss/WSJcomUSMarkets.xml",
    "https://feeds.a.dj.com/rss/WSJcomUSTechnology.xml",
    "https://feeds.a.dj.com/rss/WSJcomOpinion.xml",

    # Reuters
    "https://news.google.com/rss/search?q=site%3Areuters.com&hl=en-US&gl=US&ceid=US%3Aen",
    "http://feeds.reuters.com/Reuters/worldNews",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.reuters.com/Reuters/PoliticsNews",
    "http://feeds.reuters.com/reuters/technologyNews",
    "http://feeds.reuters.com/reuters/topNews",

    # Financial Times
    "https://www.ft.com/world?format=rss",
    "https://www.ft.com/companies?format=rss",
    "https://www.ft.com/markets?format=rss",
    "https://www.ft.com/technology?format=rss",
    "https://www.ft.com/opinion?format=rss",

    # Bloomberg
    "https://feeds.bloomberg.com/industries/news.rss",
    "https://feeds.bloomberg.com/markets/news.rss",
    "https://feeds.bloomberg.com/politics/news.rss",
    "https://feeds.bloomberg.com/technology/news.rss",
    "https://feeds.bloomberg.com/wealth/news.rss",
    "https://feeds.bloomberg.com/green/news.rss",
    "https://feeds.bloomberg.com/economics/news.rss",
    "https://feeds.bloomberg.com/industries/news.rss",

    # The New York Times
    "http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/Opinion.xml",

    # NPR
    "https://feeds.npr.org/1001/rss.xml",
    "https://feeds.npr.org/1004/rss.xml",
    "https://feeds.npr.org/1014/rss.xml",
    "https://feeds.npr.org/1006/rss.xml",
    "https://feeds.npr.org/1019/rss.xml",

    # BBC News
    "http://feeds.bbci.co.uk/news/world/rss.xml",
    "http://feeds.bbci.co.uk/news/business/rss.xml",
    "http://feeds.bbci.co.uk/news/technology/rss.xml",
    "http://feeds.bbci.co.uk/news/politics/rss.xml",

    # CNN
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://rss.cnn.com/rss/cnn_world.rss",
    "http://rss.cnn.com/rss/cnn_allpolitics.rss",
    "http://rss.cnn.com/rss/money_latest.rss",
    "http://rss.cnn.com/rss/cnn_tech.rss",

    # TechMeme
    "https://www.techmeme.com/feed.xml",

    # Al Jazeera
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://www.aljazeera.com/xml/rss/economy.xml",
    "https://www.aljazeera.com/xml/rss/middleeast.xml",
    "https://www.aljazeera.com/xml/rss/asia.xml"
]

def fetch_rss_feeds():
    """Fetch headlines from multiple RSS feeds and return them as a list."""
    feed_data = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:15]:  # Limit to 15 headlines per feed
            description = entry.get('description', 'No des. available')  # Use .get() for dictionary access
            title = entry.get('title', 'No title available')  # Use .get() for dictionary access
            link = entry.get('link', 'No link avail.')
            
            feed_data.append({'title': title, 'description': description, 'link': link})
            
    return feed_data

def format_rss_for_email(rss_data):
    """Format the fetched RSS data for email."""
    formatted_data = []
    for entry in rss_data:
        formatted_data.append(f"{entry['title']}\n{entry['description']}\nRead more: {entry['link']}\n")
    return "\n".join(formatted_data)

# Update function names to match the previous script
def fetch_and_summarize_rss():
    """Fetch and summarize RSS feeds."""
    print("Fetching and summarizing RSS feeds...")
    feed_data = fetch_rss_feeds()
    summarized_data = format_rss_for_email(feed_data)
    print(f"Fetched {len(feed_data)} headlines.")
    return summarized_data
