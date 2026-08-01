import pandas as pd 

df = pd.read_csv("jobs.csv")

print(f"Total number of jobs scraped: {len(df)}")
print("-" * 50)

top_locations = df['Location'].value_counts().head(5)
print("Top 5 Location with most jobs:")
print(top_locations)
print("-"*50)

python_jobs = df[df['Job_Title'].str.contains("python" , case=False)]
print(f"Percentage of Python jobs: {(len(python_jobs)/len(df))*100:.2f}%")
print("-"*50)
print("Sample Python Job Titles:")
print(python_jobs['Job_Title'].head(3).to_string(index=False))