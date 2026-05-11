# News_discord_bot

pip install -r requirements.txt 로 작업에 필요한 라이브러리 인스톨
하고 python -m pip show requests경로 확인 
만약 경로를 찾을 수 없다면 python -m pip install -r requirements.txt 실행

A: collecter폴더 내에 뉴스 기사 RSS파일에서 기사를 수집 및 기사 형식 정규화
B: database폴더 내에 DB테이블 설계, db안에 apple,banana등의 10가지 문자열이 있을 때 새롭게 문자열 몇개를 들고왔을 때 신규,중복 판정하는 구조 제작
C: bot폴더에 디스코드 봇 토큰 연동 및 지정 채널로 테스트 메세지 전송 성공

변수 이름은 snake_case로  (단어 사이를 _로 연결하는것을 의미)

디스코봇 토큰은 깃허브에 공유 시 탈취 위험이 있으므로 .env파일에 변수로 저장해두고 꺼내서 사용 (예: DISCORD_BOT_TOKEN=your_token_here)

