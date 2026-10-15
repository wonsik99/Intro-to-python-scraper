# Job Scraper

I made this repo while learning web scraping with Python (requests and BeautifulSoup) and Flask. The final project is a small job search site: pick a skill, and it shows matching jobs from Berlin Startup Jobs, Web3 Career and We Work Remotely.

Live site: https://wonsik99.github.io/python-job-scraper/

## How it works

- `berlin_scraper.py` fetches Berlin Startup Jobs with requests and reads the listings out of the HTML with BeautifulSoup.
- `web3_wwr_scraper.py` does the same for Web3 Career. We Work Remotely blocks scrapers on its search page, so this file reads its RSS feeds and filters them by keyword instead.
- `app.py` is the Flask app. Run locally, it scrapes live for any skill you type.
- GitHub Pages can only serve files, not run Python. So Frozen-Flask renders a results page for each skill in `KEYWORDS` ahead of time, and those HTML files are what the live site shows.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run locally

```bash
python app.py
```

Open http://localhost:5001 and search for any skill.

## Update the live site

```bash
python app.py build       # scrape again and write the HTML to build/
ghp-import -n -p build    # commit build/ to the gh-pages branch and push it
```

GitHub Pages picks up the new pages a minute or two later. Job listings are only as fresh as the last build, so run both commands again whenever you want new ones. To add a skill, put it in `KEYWORDS` in `app.py` and rebuild.

## Files

| File | What it does |
|---|---|
| `app.py` | Flask app and static site build |
| `berlin_scraper.py` | Berlin Startup Jobs scraper and the `JobInfo` class |
| `web3_wwr_scraper.py` | Web3 Career and We Work Remotely scrapers |
| `templates/` | Page templates (`base.html` holds the shared layout) |

The other `.py` files are earlier exercises: Python basics, a first scraper with requests and BeautifulSoup (`static_scraper.py`), and a Playwright scraper for a JavaScript-heavy site (`dynamic_scraper.py`, which saves to `jobs.csv`).
