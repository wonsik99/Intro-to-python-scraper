from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless = False)

page = browser.new_page()

# page.goto("https://www.wanted.co.kr")
page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# # #headless mode
# # page.screenshot(path="screenshot.png")

# frame_locator = page.frame_locator("iframe.ab-in-app-message")  # iframe 선택
# frame_locator.locator("#action-button-next").click()
# frame_locator.locator("#button-close").click()

# page.click("button.Aside_searchButton__Ib5Dn.Aside_isNotMobileDevice__ko_mZ")
# # page.locator("button.Aside_searchButton__Ib5Dn.Aside_isNotMobileDevice__ko_mZ")

# time.sleep(3)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(3)

# page.keyboard.down("Enter")

# time.sleep(3)

# page.click("a#search_tab_position")

# time.sleep(3)

for x in range (3):
    page.keyboard.down("End")
    time.sleep(3)   

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_ = "JobCard_container__zQcZs JobCard_container--variant-card___dlv1")

jobs_db = []

for job in jobs:
    job_url = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_ = "JobCard_title___kfvj").text
    company_name = job.find("span", class_ = "CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu").text
    # requirement = job.find("span", class_ = "CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__location4__w0l").text
    reward = job.find("span", class_ = "JobCard_reward__oCSIQ").text


    job = {
        "title" :title,
        "company_name": company_name,
        "reward": reward,
        "link" : job_url
    }

    jobs_db.append(job)

print(jobs_db)
print(len(jobs_db))

file = open("jobs.csv", "w")
writer = csv.writer(file)
writer.writerow(
    [
        "Title", 
        "Company", 
        "Reward", 
        "Link"
    ]
)

for job in jobs_db:
    writer.writerow(job.values())
file.close()