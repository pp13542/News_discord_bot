import feedparser
import sqlite3
import discord
from dotenv import load_dotenv
import os
from discord.ext import tasks

# env 파일 로드
load_dotenv()
# RSS URL
url = "https://www.boannews.com/media/news_rss.xml"
# RSS 파싱
feed = feedparser.parse(url)
# DB 연결
news_db = sqlite3.connect("news.db")
cur = news_db.cursor()
cur.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT UNIQUE
        )
    """)
# 디스코드 정보
Token = os.getenv("Token")
news_channel_id = int(os.getenv("news_channel_id"))
client = discord.Client(intents=discord.Intents.default())

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
    feeds = parse_rss()
    cur = news_db.cursor()
    for feed in feeds:
        link = feed["link"]
        
        cur.execute("SELECT link FROM news WHERE link = ?", (link,))
        result = cur.fetchone()

        if result is None:
            feed["new"] = "o"
        else:
            feed["new"] = "x"

    return feeds

async def send_message(): #디스코드 메세지 전송
    feeds = new_verification()

    for feed in feeds:
        title = feed["title"]
        link = feed["link"]

        if feed["new"] == "o":
            channel = client.get_channel(news_channel_id)

            embed = discord.Embed(
                title="🛡 새로운 보안 뉴스",
                color=discord.Color.green()
            )

            embed.add_field(
                name="제목",
                value=title,
                inline=False
            )

            embed.add_field(
                name="링크",
                value=link,
                inline=False
            )

            await channel.send(embed=embed)

            cur.execute( #DB에 뉴스 저장
                    "INSERT INTO news (title, link) VALUES (?, ?)",
                    (title, link)
                )
            news_db.commit()

        else:
            continue

@tasks.loop(minutes=30)
async def news_loop():
    await send_message()
          
@client.event
async def on_ready():
    print("봇 실행됨")
    news_loop.start()
    
client.run(Token)
