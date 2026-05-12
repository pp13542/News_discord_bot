# Discord News Bot

RSS 기반으로 보안 뉴스를 자동 수집하여 Discord 채널로 전송하는 봇입니다.

---

## Features

- RSS 뉴스 자동 수집
- SQLite 기반 중복 뉴스 필터링
- 30분 주기 자동 실행
- Discord Embed 메시지 전송

---

## Architecture

RSS Feed → 데이터 파싱 → 중복 검사 (SQLite) → 신규 뉴스 필터링 → Discord 전송 → DB 저장

---

## Tech Stack

- Python
- discord.py
- feedparser
- SQLite3
- python-dotenv

---

## Installation

```bash
pip install -r requirements.txt