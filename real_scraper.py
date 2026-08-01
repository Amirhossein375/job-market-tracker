import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

response = requests.get(URL)

html_content = response.text
soup = BeautifulSoup(html_content , "html.parser")

job_cards = soup.find_all("div" , class_="card-content")
jobs_data = []
print("\n Extracting data from the internet...")

for card in job_cards:
    title = card.find("h2" , class_="title").text.strip()
    company = card.find("h3" , class_="company").text.strip()
    location = card.find("p" , class_="location").text.strip()
    jobs_data.append({
        "Job_Title" : title,
        "Company" : company,
        "Location" : location })

df = pd.DataFrame(jobs_data)
df.to_csv("jobs.csv" , index=False)

print(f"✅ Successfully extracted {len(df)} job listings and saved them to jobs.csv!")
