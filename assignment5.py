import re
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
from assignment4 import scrape_jobs_berlin, JobInfo, HEADERS

def scrape_web3_career(url, max_pages = 3):
    all_jobs = []
    page_count = 0
    while url and page_count < max_pages:
        page_count += 1
        response = requests.get(url, headers = HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        # The table class is now "table table-borderless jobs-table-flow",
        # so match one class instead of the exact class string
        jobs_section = soup.find("table", class_ = "table-borderless")
        if not jobs_section:
            print("jobs section not found")
            return all_jobs

        jobs = jobs_section.find_all("tr")

        for job in jobs:

            h2_tag = job.find("h2")
            if not h2_tag:
                continue
            job_title = h2_tag.text.strip()

            h3_tag = job.find("h3")
            if not h3_tag:
                continue
            company_name = h3_tag.text.strip()

            link_tag = job.find("a")
            if not link_tag:
                continue
            job_link = link_tag["href"]
            if job_link.startswith("/"):
                job_link = f"https://web3.career{job_link}"

            all_jobs.append(JobInfo(company_name, job_title, job_link))

        next_button = soup.find("li", class_="page-item next")
        next_page = next_button.find("a", class_="page-link") if next_button else None
        if next_page:
            url = f"https://web3.career{next_page['href']}"
        else:
            url = None

    return all_jobs


# The search page (weworkremotely.com/remote-jobs/search) now answers scrapers with a
# Cloudflare "Just a moment..." 403 page, even through Playwright. The RSS feeds are
# public, so read those and keep the jobs that mention the keyword.
WWR_FEEDS = [
    "https://weworkremotely.com/remote-jobs.rss",
    "https://weworkremotely.com/categories/remote-programming-jobs.rss",
    "https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss",
]

def scrape_weworkremotely(keyword):
    all_jobs = []
    seen_links = set()
    # Whole word only, so "java" doesn't match "javascript" and "rust" doesn't match "trust"
    pattern = re.compile(rf"(?<!\w){re.escape(keyword)}(?!\w)", re.IGNORECASE)

    for feed_url in WWR_FEEDS:
        response = requests.get(feed_url, headers = HEADERS)
        feed = ET.fromstring(response.content)

        for item in feed.iter("item"):
            job_link = item.findtext("link")
            if job_link in seen_links:
                continue
            seen_links.add(job_link)

            # RSS titles look like "Company: Job title"
            company_name, _, job_title = item.findtext("title", "").partition(": ")
            description = item.findtext("description", "")

            if pattern.search(job_title) or pattern.search(description):
                all_jobs.append(JobInfo(company_name, job_title, job_link))

    return all_jobs


if __name__ == "__main__":
    keyword = "python"
    berlin_jobs = scrape_jobs_berlin(f"https://berlinstartupjobs.com/skill-areas/{keyword}/")
    web3_jobs = scrape_web3_career(f"https://web3.career/{keyword}-jobs")
    wwr_jobs = scrape_weworkremotely(keyword)

    for job in berlin_jobs + web3_jobs + wwr_jobs:
        print(job)
    print(f"berlin {len(berlin_jobs)} / web3 {len(web3_jobs)} / wwr {len(wwr_jobs)}")
