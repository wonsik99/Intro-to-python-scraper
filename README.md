# Job Scrapper

A Flask app that searches three job boards for one skill at a time: Berlin Startup Jobs, Web3 Career and We Work Remotely. Built as assignment 5 of a Python web scraping course.

Live site: https://wonsik99.github.io/Intro-to-python-scraper/

## How it works

- `assignment4.py` scrapes Berlin Startup Jobs.
- `assignment5.py` scrapes Web3 Career and reads the We Work Remotely RSS feeds. Their search page blocks scrapers, so the feeds are filtered by keyword instead.
- `assignment5_flask.py` is the Flask app. Run locally, it scrapes live for any skill you type.
- GitHub Pages can only serve files, not run Python. So Frozen-Flask renders a results page for each skill in `KEYWORDS` ahead of time, and those HTML files are what the live site shows.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run locally

```bash
python assignment5_flask.py
```

Open http://localhost:5001 and search for any skill.

## Update the live site

```bash
python assignment5_flask.py build   # scrape again and write the HTML to build/
ghp-import -n -p build              # commit build/ to the gh-pages branch and push it
```

GitHub Pages picks up the new pages a minute or two later. Job listings are only as fresh as the last build, so run both commands again whenever you want new ones. To add a skill, put it in `KEYWORDS` in `assignment5_flask.py` and rebuild.

## Files

| File | What it does |
|---|---|
| `assignment4.py` | Berlin Startup Jobs scraper and the `JobInfo` class |
| `assignment5.py` | Web3 Career and We Work Remotely scrapers |
| `assignment5_flask.py` | Flask app and static site build |
| `templates/` | Page templates (`base.html` holds the shared layout) |

The other `.py` files are earlier exercises from the course.
