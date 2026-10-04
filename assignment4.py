
# BLUEPRINT | DONT EDIT

import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://berlinstartupjobs.com/engineering/",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

skills = ["python", "typescript", "javascript", "rust"]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:

# /YOUR CODE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

class JobInfo:
    def __init__(self, company_name, job_title, job_link, job_description):
        self.company_name = company_name
        self.job_title = job_title
        self.job_link = job_link
        self.job_description = job_description

    def __str__(self):
        return (
            f"Company: {self.company_name}\n"
            f"Job title: {self.job_title}\n"
            f"Job link: {self.job_link}\n"
            f"Job description: {self.job_description}\n"
            + "-"*50
        )

def scrape_jobs(url):
    all_jobs = []
    while url:
        response = requests.get(url, headers = HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        jobs_section = soup.find("ul", class_ = "jobs-list-items")
        if not jobs_section:
            print("jobs section not found")
            exit()

        jobs = jobs_section.find_all("li", class_ = "bjs-jlid")

        for job in jobs:
            job_title_section = job.find("h4", class_ = "bjs-jlid__h")
            job_title = job_title_section.find("a").text
            job_link = job_title_section.find("a")["href"]
            company_name = job.find("a", class_ = "bjs-jlid__b").text
            job_description = job.find("div", class_ = "bjs-jlid__description").text.strip()
            all_jobs.append(JobInfo(company_name, job_title, job_link, job_description))

        next_button = soup.find("a", class_ = "next page-numbers")
        if next_button:
            url = next_button["href"]
        else:
            url = None
        

    return all_jobs

all_jobs = scrape_jobs("https://berlinstartupjobs.com/engineering/")

skills = ["python", "typescript", "javascript"]

for skill in skills:
    skill_url = f"https://berlinstartupjobs.com/skill-areas/{skill}/"
    all_jobs.extend(scrape_jobs(skill_url))

for job in all_jobs:
    print(job)