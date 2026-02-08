from scrapers.berlin_startup_jobs import scrape_jobs_berlin
from scrapers.web3_career import scrape_web3_career
from scrapers.weworkremotely import scrape_weworkremotely

# Main execution
result_jobs = []
# skills = ["python", "typescript", "javascript", "rust"]
skills = ["python"]

for skill in skills:
    print(f"Scraping {skill} jobs...")
    
    # Berlin Startup Jobs
    berlin_url = f"https://berlinstartupjobs.com/skill-areas/{skill}/"
    result_jobs.extend(scrape_jobs_berlin(berlin_url))
    print("berlin done")
    
    # Web3 Career
    web3_career_url = f"https://web3.career/{skill}-jobs"
    result_jobs.extend(scrape_web3_career(web3_career_url))
    print("web3 done")
    
    # We Work Remotely
    weworkremotely_url = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={skill}"
    result_jobs.extend(scrape_weworkremotely(weworkremotely_url))
    print("we work done")

# Print all jobs
for job in result_jobs:
    print(job)
