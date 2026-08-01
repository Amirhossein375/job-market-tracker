# Job Market Tracker (Web Scraper & Analytics)

A Python-based data engineering project that automates the process of extracting, cleaning, storing, and analyzing job market postings from web portals.

## 🚀 Project Overview

This project consists of an end-to-end data collection and analysis pipeline:
1. **Web Scraping:** Downloads and parses live job postings using the Python `requests` library and `BeautifulSoup`.
2. **Data Storage:** Cleans and structured the raw text, then stores the dataset into a relational CSV format using `Pandas`.
3. **Exploratory Data Analysis (EDA):** Performs automated statistical analysis to find top hiring locations and calculate the demand/percentage for specific programming languages (such as Python).

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries:** BeautifulSoup4, Requests, Pandas
* **Environment:** Virtual Environments (`venv`)

## ⚙️ Installation & Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<your-username>/job-market-tracker.git
   cd job-market-tracker
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Scraping Pipeline:**
   This script scrapes 100 job postings from the sandbox portal and saves them to `jobs.csv`.
   ```bash
   python real_scraper.py
   ```

5. **Run the Analytics Pipeline:**
   This script parses the CSV dataset and prints key analytics (Top locations, Python job demand percentage).
   ```bash
   python analyze_jobs.py
   ```
