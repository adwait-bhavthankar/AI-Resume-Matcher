import streamlit as st
import os
import pandas as pd
from utils import extract_text_from_pdf, score_resume_against_job, load_job_description

st.set_page_config(page_title="AI Resume Matcher", layout="wide")
st.title("🤖 Resume Matching with AI + Mistral via Ollama")

# Load all job descriptions
job_df = load_job_description("data/job_description.csv")

# File upload
uploaded_file = st.file_uploader("Upload a Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    os.makedirs("data/resumes", exist_ok=True)
    resume_path = os.path.join("data/resumes", uploaded_file.name)
    with open(resume_path, "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text_from_pdf(resume_path)
    st.info("Running AI model against all job roles...")

    results = []

    for _, row in job_df.iterrows():
        job_title = row["Job Title"]
        job_description = row["Job Description"]
        response = score_resume_against_job(resume_text, job_description)

        results.append({
            "Job Title": job_title,
            "Match Report": response
        })

    st.success("✅ Matching complete!")

    for res in results:
        with st.expander(f"📌 {res['Job Title']}"):
            st.text(res["Match Report"])

    # Optional: Download report as CSV
    result_df = pd.DataFrame(results)
    csv = result_df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Results as CSV", data=csv, file_name="resume_matching_results.csv", mime="text/csv")
