import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# jobs = soup.find("section", class_ = "jobs").find_all("li")[0:-1]

# jobs_section = soup.find("section", id="job_listings") or soup.find("section", class_="jobs")
# if not jobs_section:
#     print("❌ jobs section not found")
#     exit()

# jobs = jobs_section.find_all("li", class_="new-listing-container")

# for job in jobs:
#     title = job.find("h3", class_ ="new-listing__header__title").text.strip()
#     if not title:
#         continue

#     company = job.find("p", class_="new-listing__company-name").text.strip()

#     categories = job.find_all("p", class_="new-listing__categories__category")
#     position = categories[0].text.strip() if categories else "N/A"
#     region = categories[-1].text.strip() if categories else "N/A"
    

#     print(title,"|", company,"|", position,"|", region,"|\n")


# 1️⃣ jobs section 찾기 (id 또는 class)
jobs_section = soup.find("section", id="job_listings") or soup.find("section", class_="jobs")
if not jobs_section:
    print("❌ jobs section not found")
    exit()

# 2️⃣ 실제 채용 공고만 가져오기
jobs = jobs_section.find_all("li", class_="new-listing-container")

for job in jobs:
    # 3️⃣ title
    title_tag = job.find("h3", class_="new-listing__header__title")
    if not title_tag:
        continue
    title = title_tag.text.strip()

    # 4️⃣ company
    company_tag = job.find("p", class_="new-listing__company-name")
    company = company_tag.text.strip() if company_tag else "N/A"

    # 5️⃣ categories 처리 (Featured 제외)
    categories = [
        c for c in job.find_all("p", class_="new-listing__categories__category")
        if "new-listing__categories__category--featured" not in c.get("class", [])
    ]

    # 6️⃣ position, region 추출
    position = "N/A"
    region = "N/A"
    for cat in categories:
        text = cat.text.strip()
        # 직무 형태
        if text.lower() in ["full-time", "part-time", "contract", "intern"]:
            position = text
        # 지역
        elif "anywhere" in text.lower() or "remote" in text.lower() or "world" in text.lower():
            region = text

    print(f"{title} | {company} | {position} | {region} |")
