class JobInfo:
    def __init__(self, company_name, job_title, job_link):
        self.company_name = company_name
        self.job_title = job_title
        self.job_link = job_link

    def __str__(self):
        return (
            f"Company: {self.company_name}\n"
            f"Job title: {self.job_title}\n"
            f"Job link: {self.job_link}\n"
            + "-"*50
        )

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
