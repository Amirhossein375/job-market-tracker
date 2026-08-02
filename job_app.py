import streamlit as pd_st
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Job Market Tracker" , page_icon="💼" , layout="wide")

st.title("Job Market Analytics Tracker:")
st.write("Analyzing in-demand skills and job postings scraped from the web:")

@st.cache_data
def load_data():
    return pd.read_csv("jobs_detailed.csv")

df = load_data()

col1 , col2 = st.columns(2)
with col1:
    st.metric("Total Jobs Scraped" , len(df))
with col2 :
    python_count = df['Job_Title'].str.contains("python" , case=False).sum()
    st.metric("Python-Related Jobs" , python_count)

st.divider()

st.subheader("Top In-Demand Skills")
target_skills = ['python' , 'django' , 'docker' , 'css' , 'html' , 'scrum' , 'agile']
skill_counts = {}

for skill in target_skills:
    count = df['Description'].str.contains(skill , case=False , na=False).sum()
    skill_counts[skill.capitalize()]=count

skills_df = pd.DataFrame(list(skill_counts.items()), columns=['Skill' , 'Demand_Count']).sort_values(by="Demand_Count" , ascending=False)
st.bar_chart(data=skills_df , x="Skill" , y="Demand_Count")

st.divider()

st.subheader("Interactive Job Search")
search_query = st.text_input("Search job title or companies:")

if search_query:
    filtered_df = df[df["Job_Title"].str.contains(search_query , case=False) | df["Company"].str.contains(search_query,case=False)]
else:
    filtered_df =df

st.dataframe(filtered_df[['Job_Title' , 'Company' , 'Location']], use_container_width=True)

st.divider()
st.subheader("View Job Description & Apply")
selected_job = st.selectbox("Select a job to view details" , df['Job_Title'].unique())

if selected_job:
    job_info = df[df["Job_Title"] == selected_job].iloc[0]

    st.markdown(f"### {job_info['Job_Title']} @ **{job_info['Company']}**")
    st.caption(f"📍Location : {job_info['Location']}")
    st.info(job_info['Description'])
    st.markdown(f"[🔗Apply to this Job]({job_info['Detail_Link']})")