import feedparser

url = "https://www.boannews.com/media/news_rss.xml"
feed = feedparser.parse(url) # url안의 xml파일을 

def parse_rss():
    feed_list = []
    feed_dict = {}
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        feed_dict = {"title": title, "link": link}
        feed_list.append(feed_dict)
    return feed_list

print(parse_rss()[0])
