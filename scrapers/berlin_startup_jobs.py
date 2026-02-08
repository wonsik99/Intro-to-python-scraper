import requests
from bs4 import BeautifulSoup
from job_info import JobInfo, HEADERS

def scrape_jobs_berlin(url):
    all_jobs = []
    while url:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        jobs_section = soup.find("ul", class_="jobs-list-items")
        if not jobs_section:
            print("jobs section not found")
            return all_jobs # Return empty list instead of exit() so other scrapers can run

        jobs = jobs_section.find_all("li", class_="bjs-jlid")

        for job in jobs:
            job_title_section = job.find("h4", class_="bjs-jlid__h")
            job_title = job_title_section.find("a").text
            job_link = job_title_section.find("a")["href"]
            company_name = job.find("a", class_="bjs-jlid__b").text
            # Description scraped but not used in JobInfo(company, title, link) as per assignment5 usage logic
            # job_description = job.find("div", class_="bjs-jlid__description").text.strip()
            
            all_jobs.append(JobInfo(company_name, job_title, job_link))

        next_button = soup.find("a", class_="next page-numbers")
        if next_button:
            url = next_button["href"]
        else:
            url = None
        
    return all_jobs

if __name__ == "__main__":
    skills = ["python"]
    for skill in skills:
        skill_url = f"https://berlinstartupjobs.com/skill-areas/{skill}/"
        jobs = scrape_jobs_berlin(skill_url)
        for job in jobs:
            print(job)