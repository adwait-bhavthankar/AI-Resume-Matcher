import pdfplumber
import pandas as pd
from ollama_client import query_ollama  # or however you invoke mistral

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def score_resume_against_job(resume_text, job_description):
    prompt = f"""
Compare the following candidate resume with the job description. 

1. Give a match score out of 100.
2. Highlight key strengths.
3. Point out skill gaps.
4. Suggest improvements.
5. Provide a summary.

---

Job Description:
{job_description}

---

Resume:
{resume_text}

---

Respond in the following format:

Match Score: 
Strengths: 
Weaknesses: 
Suggestions: 
Summary:
"""
    return query_ollama(prompt)

def load_job_description(csv_path):
    df = pd.read_csv(csv_path, encoding="latin1")
    return df[["Job Title", "Job Description"]].dropna()
