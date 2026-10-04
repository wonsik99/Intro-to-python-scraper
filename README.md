# Job Scrapper

Berlin Startup Jobs, Web3 Career, We Work Remotely에서 키워드로 채용 공고를 모아 보여주는 Flask 앱입니다 (assignment 5).

사이트: https://wonsik99.github.io/Intro-to-python-scraper/

## 처음 한 번만: 설치

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 내 컴퓨터에서 실행

```bash
python assignment5_flask.py
```

http://localhost:5001 에서 아무 키워드나 실시간으로 검색할 수 있습니다.

## GitHub Pages에 배포

GitHub Pages는 HTML 파일만 보여줄 수 있고 파이썬은 실행하지 못합니다. 그래서 `assignment5_flask.py`의 `KEYWORDS`에 있는 키워드만 미리 스크래핑해서 HTML로 만들고(Frozen-Flask), 그 파일들을 `gh-pages` 브랜치에 올립니다.

```bash
python assignment5_flask.py build   # build/ 폴더에 HTML 생성
ghp-import -n -p build              # build/ 내용을 gh-pages 브랜치에 커밋하고 push
```

1~2분 뒤 사이트에 반영됩니다. 공고는 build한 날 기준이라, 새 공고를 보려면 위 두 줄을 다시 실행하면 됩니다. 키워드를 추가하려면 `KEYWORDS` 리스트에 넣고 다시 build → 배포하세요.

## 파일

| 파일 | 내용 |
|---|---|
| `assignment4.py` | Berlin Startup Jobs 스크래퍼, `JobInfo` 클래스 |
| `assignment5.py` | Web3 Career, We Work Remotely 스크래퍼 |
| `assignment5_flask.py` | Flask 앱 + 정적 사이트 빌드 |
| `templates/` | 홈, 검색 결과 HTML |
