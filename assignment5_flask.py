from flask import Flask, render_template, request
from assignment4 import scrape_jobs_berlin
from assignment5 import scrape_web3_career, scrape_weworkremotely

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="nico")

@app.route("/search")
def search():
    keyword = request.args.get("keyword").strip().lower()
    result_jobs = []

    print(f"Scraping jobs for: {keyword} ...")

    # Berlin Startup Jobs
    berlin_url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
    result_jobs.extend(scrape_jobs_berlin(berlin_url))
    print("Berlin done")

    # Web3 Career
    web3_url = f"https://web3.career/{keyword}-jobs"
    result_jobs.extend(scrape_web3_career(web3_url))
    print("Web3 done")

    # We Work Remotely
    wework_url = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={keyword}"
    result_jobs.extend(scrape_weworkremotely(wework_url))
    print("WWR done")

    # for job in result_jobs:
    #     print(job)

    return render_template("search.html", jobs=result_jobs, keyword=keyword)


app.run("0.0.0.0", port=5001)