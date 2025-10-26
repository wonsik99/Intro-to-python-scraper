import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# find jobs section
jobs_section = soup.find("section", id="job_listings") or soup.find("section", class_="jobs")
if not jobs_section:
    print("❌ jobs section not found")
    exit()

jobs = jobs_section.find_all("li", class_="new-listing-container")

for job in jobs:
    title_tag = job.find("h3", class_="new-listing__header__title")
    if not title_tag:
        continue
    title = title_tag.text.strip()

    company_tag = job.find("p", class_="new-listing__company-name")
    company = company_tag.text.strip() if company_tag else "N/A"

    categories = [
        c for c in job.find_all("p", class_="new-listing__categories__category")
        if "new-listing__categories__category--featured" not in c.get("class", [])
    ]

    position = "N/A"
    region = "N/A"
    for cat in categories:
        text = cat.text.strip()
        if text.lower() in ["full-time", "part-time", "contract", "intern"]:
            position = text
        elif "anywhere" in text.lower() or "remote" in text.lower() or "world" in text.lower():
            region = text

    print(f"{title} | {company} | {position} | {region} |")
