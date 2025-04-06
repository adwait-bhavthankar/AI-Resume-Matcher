import streamlit as st
import os
from utils import extract_text_from_pdf, score_resume_against_job, load_job_description

st.set_page_config(page_title="AI Resume Matcher", layout="wide")

st.title("🤖 Resume Matching with AI + Ollama")

job_description = load_job_description("data/job_description.csv")

uploaded_file = st.file_uploader("Upload a Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    with open(f"data/resumes/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())

    resume_path = f"data/resumes/{uploaded_file.name}"
    resume_text = extract_text_from_pdf(resume_path)

    st.info("Running AI model...")

    result = score_resume_against_job(resume_text, job_description)
    st.markdown("### ✅ AI Analysis:")
    st.markdown(result)
