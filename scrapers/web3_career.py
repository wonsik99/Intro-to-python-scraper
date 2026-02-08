import requests
from bs4 import BeautifulSoup
from job_info import JobInfo, HEADERS

def scrape_web3_career(url):
    all_jobs = []
    while url:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        jobs_section = soup.find("table", class_="table table-borderless")
        if not jobs_section:
            print("jobs section not found")
            return all_jobs

        jobs = jobs_section.find_all("tr")

        for job in jobs:
            
            h2_tag = job.find("h2")
            if not h2_tag:
                continue
            job_title = h2_tag.text
            
            h3_tag = job.find("h3")
            if not h3_tag:
                continue
            company_name = h3_tag.text.strip()
            
            job_link = url
            
            all_jobs.append(JobInfo(company_name, job_title, job_link))

        next_button = soup.find("li", class_="page-item next")
        if next_button is None:
            url = None
            continue
        next_page = next_button.find("a", class_="page-link")
        if next_page:
            url = f"https://web3.career{next_page['href']}"
        else:
            url = None

    return all_jobs

if __name__ == "__main__":
    skills = ["python"]
    for skill in skills:
        url = f"https://web3.career/{skill}-jobs"
        jobs = scrape_web3_career(url)
        for job in jobs:
            print(job)