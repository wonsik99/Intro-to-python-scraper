from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
    )

results = {}

for website in websites:
    if not website.startswith("https://"):
        # print("have to fix")
        website = f"https://{website}"
    response = get(website)
    # print(response.status_code)
    if response.status_code == 200:
        # print(f"{website} is ok")
        results[website] = "OK"
    else:
        # print(f"{website} not ok")
        results[website] = "FAILED"

print(results)

