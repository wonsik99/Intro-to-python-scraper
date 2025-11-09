from turtle import title
import requests
from bs4 import BeautifulSoup
from assignment4 import scrape_jobs_berlin, JobInfo, HEADERS
from playwright.sync_api import sync_playwright

def scrape_web3_career(url):
    all_jobs = []
    while url:
        response = requests.get(url, headers = HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        jobs_section = soup.find("table", class_ = "table table-borderless")
        if not jobs_section:
            print("jobs section not found")
            exit()

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

        url = f"https://web3.career{next_page["href"]}"
        # print(f"page {next_page["href"]}")
        

    return all_jobs


def scrape_weworkremotely(url):
    all_jobs = []
    
    p = sync_playwright().start()
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()

    page.goto(url)

    content = page.content()

    p.stop()

    soup = BeautifulSoup(content, "html.parser")
    jobs_section = soup.find("div", id="search-results")
    # print(jobs_section)
    if not jobs_section:
        print("jobs section not found")
        exit()

    jobs = jobs_section.find_all("li", class_="new-listing-container")
    if not jobs:
            print("jobs  not found")

    for job in jobs:
        title_tag = job.find("h3", class_="new-listing__header__title")
        if not title_tag:
            print("wrong")
            continue
        job_title = title_tag.text
        
        company_tag = job.find("p", class_="new-listing__company-name")
        if not company_tag:
            continue
        company_name = company_tag.text.strip()
        
        job_link = url
        
        all_jobs.append(JobInfo(company_name, job_title, job_link))

    return all_jobs


# # Main execution
# result_jobs = []
# # skills = ["python", "typescript", "javascript", "rust"]
# skills = ["python"]

# for skill in skills:
#     print(f"Scraping {skill} jobs...")
    
#     # Berlin Startup Jobs
#     berlin_url = f"https://berlinstartupjobs.com/skill-areas/{skill}/"
#     result_jobs.extend(scrape_jobs_berlin(berlin_url))
#     print("berline done")
    
#     # Web3 Career
#     web3_career_url = f"https://web3.career/{skill}-jobs"
#     result_jobs.extend(scrape_web3_career(web3_career_url))
#     print("web3 done")
    
#     # We Work Remotely
#     weworkremotely_url = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={skill}"
#     result_jobs.extend(scrape_weworkremotely(weworkremotely_url))
#     print("we work done")

# # Print all jobs
# for job in result_jobs:
#     print(job)
