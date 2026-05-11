import requests

url = "https://www.boannews.com/media/news_rss.xml"

def get_news():
    response = requests.get(url)
    response.encoding = "euc-kr"
    news_list = response.text
    return news_list

rss = get_news()
