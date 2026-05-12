import feedparser
import sqlite3

url = "https://www.boannews.com/media/news_rss.xml"
feed = feedparser.parse(url)
news_db = sqlite3.connect("news.db")
cur = news_db.cursor()
cur.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT UNIQUE
        )
    """)

def parse_rss(): #RSS정규화
    feed_list = []
    feed_dict = {}
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        feed_dict = {"title": title, "link": link}    
        feed_list.append(feed_dict)
    return feed_list



def new_verification(): #신규 뉴스 검증
    feed_list = parse_rss()
    cur = news_db.cursor()
    for feed in feed_list:
        link = feed["link"]
        
        cur.execute("SELECT link FROM news WHERE link = ?", (link,))
        result = cur.fetchone()

        if result is None:
            feed["new"] = "o"
        else:
            feed["new"] = "x"

    return feed_list

result = new_verification()

for news in result:
    print(news)