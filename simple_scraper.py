from bs4 import BeautifulSoup


with open("mock_jobs.html" , 'r' , encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content , "html.parser")
job_cards = soup.find_all("div" , class_="job-card")

print("\n Starting job ad extraction:")
for card in job_cards:
    title = card.find("h2" , class_="job-title").text
    company = card.find("p" , class_="company").text
    salary = card.find("p" , class_ ="salary").text

    skills_list = card.find('ul' , class_="skills").find_all("li")
    skills = [li.text for li in skills_list]

    
    print(f" Job Title: {title}")
    print(f" Company: {company}")
    print(f" Salary: {salary}")
    print(f" Skills Needed: {', '.join(skills)}")
    print("-" * 40)