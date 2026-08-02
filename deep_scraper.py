import requests
import time
import pandas as pd 
from bs4 import BeautifulSoup
from tqdm import tqdm

URL = "https://realpython.github.io/fake-jobs/"
response = requests.get(URL)
soup = BeautifulSoup(response.text , "html.parser")

job_cards = soup.find_all("div" , class_="card-content")
print("\nStarting deep scraping (extracting job descriptions from internal pages):")
jobs_data = []
for card in tqdm(job_cards , desc="Scraping Jobs"):
    title = card.find("h2" , class_="title").text.strip()
    company = card.find("h3" , class_="company").text.strip()
    location = card.find("p", class_="location").text.strip()

    links = card.find_all("a" , class_="card-footer-item")
    apply_link = links[1]["href"]

    try:
        detail_response = requests.get(apply_link, timeout=5)
        detail_soup = BeautifulSoup(detail_response.text, "html.parser")
        description = detail_soup.find("div", class_="content").find("p").text.strip()
    except Exception as e:
        description = "Error fetching description"
        
    jobs_data.append({
        "Job_Title": title,
        "Company": company,
        "Location": location,
        "Detail_Link": apply_link,
        "Description": description
    })
    
    time.sleep(1)
df = pd.DataFrame(jobs_data)
df.to_csv("jobs_detailed.csv" , index=False)
print("succsseful")