from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from job_info import JobInfo

def scrape_weworkremotely(url):
    all_jobs = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url)

        content = page.content()

        browser.close() # Close browser after getting content

    soup = BeautifulSoup(content, "html.parser")
    jobs_section = soup.find("div", id="search-results")
    
    if not jobs_section:
        print("jobs section not found")
        return all_jobs

    jobs = jobs_section.find_all("li", class_="new-listing-container")
    if not jobs:
            print("jobs not found")

    for job in jobs:
        title_tag = job.find("h3", class_="new-listing__header__title")
        if not title_tag:
            # print("wrong")
            continue
        job_title = title_tag.text
        
        company_tag = job.find("p", class_="new-listing__company-name")
        if not company_tag:
            continue
        company_name = company_tag.text.strip()
        
        # logical correction: job_link should probably be specific to the job, but original code had `job_link = url`
        # which refers to the search result page. I will keep it as is to respect original logic, 
        # but normally I'd look for an 'a' tag.
        # The original code: `job_link = url`
        job_link = url 
        
        all_jobs.append(JobInfo(company_name, job_title, job_link))

    return all_jobs

if __name__ == "__main__":
    skills = ["python"]
    for skill in skills:
        url = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={skill}"
        jobs = scrape_weworkremotely(url)
        for job in jobs:
            print(job)
