import pandas as pd 

df = pd.read_csv("jobs_detailed.csv")

target_skills = ['python' , 'django' , 'docker' , 'css' , 'html' , 'scrum' , 'agile']
skill_counts = {}

for skill in target_skills:
    has_skill = df['Description'].str.contains(skill , case=False , na=False)
    count = has_skill.sum()
    skill_counts[skill.capitalize()] = count

skill_series = pd.Series(skill_counts).sort_values(ascending=False)
print("Demand for Skills in Job Market :")
print('-'*50)
for skill , count in skill_series.items():
    percentage = (count / len(df))*100
    print(f"{skill} : {count} jobs ({percentage:.1f}%)")
print("-"*40)
