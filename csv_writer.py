"""
CSV Writer Module for dynamic_scraper.py

This module provides functionality to save job posting information to CSV files.
It saves job posting data from a jobs_db list to a file in CSV format.
"""

import csv

def save_to_file(file_name, jobs_db):
    file = open(f"{file_name}.csv", "w")
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