import requests

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
    )

for website in websites:
    if not website.startswith("https://"):
        # print("have to fix")
        website = f"https://{website}"
    print(website)