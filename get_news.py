import feedparser
from datetime import datetime

def fetch_top_news(feed_url, count=5):
    feed = feedparser.parse(feed_url)
    news_items = []
    for entry in feed.entries[:count]:
        news_items.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary
        })
    return news_items

if __name__ == "__main__":
    url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    news = fetch_top_news(url)
    date = datetime.now().strftime("%Y-%m-%d")
    with open(f"news/news_{date}.md", "w", encoding="utf-8") as f:
        for i, item in enumerate(news, start=1):
            f.write(f"### {i}. {item['title']}\n")
            f.write(f"{item['summary']}\n")
            f.write(f"[Read more]({item['link']})\n\n")
