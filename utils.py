import pdfplumber
import os
import pandas as pd
from ollama_client import query_ollama

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def score_resume_against_job(resume_text, job_description):
    prompt = f"""
You are a hiring AI assistant. Compare the following resume against the job description below.
Give:
1. Match Score (out of 100)
2. Candidate Strengths
3. Candidate Weaknesses
4. Suggestions for Improvement

Resume:
{resume_text}

Job Description:
{job_description}
"""
    return query_ollama(prompt)

def load_job_description(csv_path):
    df = pd.read_csv(csv_path,encoding='latin1')
    return df.iloc[0]["Job Description"]  # or loop through roles
