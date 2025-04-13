# 🧠 MatchGenie – AI-Powered Resume Matcher (Ollama + Mistral)

This project is a smart, AI-powered resume screening tool that allows recruiters or hiring teams to compare resumes against job descriptions. It uses **local LLM inference via Ollama** running the `phi` model, providing fast and private resume analysis without sending data to the cloud.

## 🔍 Features

- Upload multiple resumes (PDF format)
- Upload job descriptions (CSV format)
- Get AI-generated:
  - ✅ Match score
  - ✅ Candidate strengths
  - ✅ Weaknesses
  - ✅ Suggestions for improvement
- Semantic analysis using **Ollama + Mistral**
- Streamlit-based interactive UI
- Dashboard-style result display

---

## 📸 Demo

![demo-screenshot](https://via.placeholder.com/800x400?text=Demo+Screenshot)

---

## ⚙️ Tech Stack

- 🧠 [Ollama](https://ollama.com) (Local LLM Runtime)
- 🤖 `phi` model for semantic resume matching
- 📄 Streamlit (Frontend)
- 🐼 Pandas (CSV handling)
- 📄 PyMuPDF (PDF parsing)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ai-resume-matcher.git
cd ai-resume-matcher
```

### 2️⃣ Install Python Packages

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
# Activate (Windows)
.env\Scriptsctivate
# Activate (Linux/Mac)
source venv/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Ollama & Run Phi Model

#### 📥 Install Ollama
Download and install Ollama:  
👉 https://ollama.com/download

#### 🧠 Pull the `phi` Model

```bash
ollama pull mistral
```

#### ▶️ Start the model in background

```bash
ollama run mistral
```

This command runs the `mistral` model locally — it will stay running in the background to serve responses.

---

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser (usually at http://localhost:8501)

---

## 📂 File Structure

```
ai-resume-matcher/
│
├── app.py                    # Main Streamlit app
├── utils.py                  # Helper functions (score logic, PDF reader)
├── ollama_client.py          # LLM query handler
├── requirements.txt          # Python dependencies
├── README.md                 # You're reading it 🙂
├── data/
│   ├── job_description.csv   # Example job description
│   └── resumes/              # Folder to drop PDF resumes
└── .gitignore
```

---

## 📌 Notes

- This app is designed to work **offline** with **local AI inference** using Ollama.
- `mistral` is a smaller, efficient language model — great for local use without heavy GPU requirements.
- All resume/job data stays on your machine — no cloud API calls involved.

---

## 📜 License

MIT License © 2025 [Your Name]

---

## 🙋‍♀️ Contribution

PRs are welcome! Please open issues if you find bugs or want new features.

---

## ❤️ Acknowledgements

- [Ollama](https://ollama.com) for providing easy-to-use LLMs locally
- [Streamlit](https://streamlit.io) for building elegant UIs with minimal code
