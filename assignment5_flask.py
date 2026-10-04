import sys
from datetime import date
from flask import Flask, render_template
from flask_frozen import Freezer
from assignment4 import scrape_jobs_berlin
from assignment5 import scrape_web3_career, scrape_weworkremotely

# Keywords that get a pre-built page on GitHub Pages
KEYWORDS = ["python", "typescript", "javascript", "rust"]

app = Flask(__name__)
app.config["FREEZER_DESTINATION"] = "build"
freezer = Freezer(app)

@app.route("/")
def home():
    return render_template("home.html", keywords=KEYWORDS, static_site=app.config.get("STATIC_SITE", False))

# /search/python/ instead of /search?keyword=python:
# GitHub Pages can only serve files, and a path can become a file (search/python/index.html)
@app.route("/search/<keyword>/")
def search(keyword):
    keyword = keyword.strip().lower()

    print(f"Scraping jobs for: {keyword} ...")

    jobs_by_site = {
        "Berlin Startup Jobs": scrape(scrape_jobs_berlin, f"https://berlinstartupjobs.com/skill-areas/{keyword}/"),
        "Web3 Career": scrape(scrape_web3_career, f"https://web3.career/{keyword}-jobs"),
        "We Work Remotely": scrape(scrape_weworkremotely, keyword),
    }
    total = sum(len(jobs) for jobs in jobs_by_site.values())

    return render_template("search.html", keyword=keyword, jobs_by_site=jobs_by_site, total=total, updated=date.today())

def scrape(scraper, target):
    # If one site breaks, show 0 jobs for it instead of breaking the whole page
    try:
        jobs = scraper(target)
    except Exception as error:
        print(f"{scraper.__name__} failed: {error}")
        return []
    print(f"{scraper.__name__}: {len(jobs)} jobs")
    return jobs

# Tells Frozen-Flask which /search/<keyword>/ pages to build
@freezer.register_generator
def search_pages():
    for keyword in KEYWORDS:
        yield "search", {"keyword": keyword}


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        # python assignment5_flask.py build -> static HTML files in build/
        app.config["STATIC_SITE"] = True
        freezer.freeze()
        print("Done! The static site is in build/")
    else:
        # python assignment5_flask.py -> live search at http://localhost:5001
        app.run("0.0.0.0", port=5001)
