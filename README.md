# 🤖 Cold Email Generator using RAG + LLM + Streamlit UI

A powerful industry-grade application that leverages **Retrieval-Augmented Generation (RAG)** to generate highly personalized and context-aware cold emails from job postings.

Built by a **fresher**, this project demonstrates real-world integration of LLMs, vector databases, prompt engineering, and web scraping — all deployed through a polished Streamlit interface.

---

## 🚀 Project Highlights

| Feature | Description |
|--------|-------------|
| 🧠 **LLM Integration** | Uses `Groq` with `deepseek-r1-distill-llama-70b` for ultra-fast, intelligent generation |
| 🌐 **Web Scraper Loader** | Loads and cleans job descriptions from external URLs using LangChain |
| 🔍 **Vector Search with ChromaDB** | Semantically matches job requirements with user portfolio projects |
| ✍️ **Advanced Prompt Engineering** | Custom-designed prompts for structured JSON output and email generation |
| 🖼️ **Streamlit UI** | Branded UI with logo, custom CSS, and responsive layout |
| 📤 **Production Ready** | Modular, secure, scalable with `.env`, prompt fallback, and Streamlit Cloud compatibility |

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| 💬 LLM | [Groq](https://groq.com/) API using LLaMA 70B |
| ⚙️ Framework | LangChain for chaining and document parsing |
| 📂 Vector Store | ChromaDB for semantic retrieval |
| 🌐 Scraper | WebBaseLoader from `langchain_community` |
| 🎨 UI | Streamlit + Custom CSS Branding |
| 🔐 Secrets | `.env` + `python-dotenv` |
| 📦 Packaging | `requirements.txt` + modular folder structure |

---

## 📁 Project Structure

```
rag-cold-email-app/
├── app/
│   ├── main.py             # Streamlit logic
│   ├── chains.py           # Prompt templates & LLM logic
│   ├── portfolio.py        # ChromaDB indexing & retrieval
│   └── utils.py            # Text cleanup helpers
├── assets/
│   ├── logo.png            # Branding logo
│   └── custom.css          # Streamlit UI styling
├── data/
│   └── sample_portfolio.csv  # Portfolio project data
├── .streamlit/
│   └── config.toml         # UI theme settings
├── .env                    # API keys (GROQ)
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── .gitignore              # Git exclusions
```

---

## 🧪 How It Works

1. Paste a job posting URL into the app.
2. The scraper loads and cleans the content.
3. LLM extracts structured job details (role, experience, skills, description).
4. Skills are matched to portfolio links stored in ChromaDB.
5. A custom cold email is generated using Groq-powered LLM.
6. Email is displayed alongside LLM reasoning (`<think>...</think>` block).

---

## 📜 Example Output

**Input Job URL:**
```
https://wadhwaniai.hire.trakstar.com/jobs/fk0p86m?utm_campaign=google_jobs_apply
```

**Generated Email:**
```
Subject: Elevate Your AI Solutions with Expertise in Speech Processing & Machine Learning

Hi [Hiring Manager's Name],

I came across your job posting for an Associate Machine Learning Scientist and was impressed by your commitment to building AI solutions...
```

**LLM Reasoning (`<think>`):**
```xml
<think>
The role is for an Associate ML Scientist with 2+ years of experience...
Portfolio match: Project 4 and Project 7
Structure: Greeting → Hook → Relevance → Portfolio → CTA → Signature
</think>
```

---

## 💼 How to Add to Your Resume

```
🔹 Built an end-to-end RAG-powered cold email generation tool using Groq, LangChain, ChromaDB, and Streamlit
🔹 Implemented document scraping, semantic search, and prompt-driven LLM pipelines
🔹 Delivered a fully-branded, production-grade Streamlit UI
🔹 Generated personalized outreach emails from unstructured job descriptions
```

---

## 🧩 Installation

```bash
git clone https://github.com/your-username/rag-cold-email-app.git
cd rag-cold-email-app
pip install -r requirements.txt
streamlit run app/main.py
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 📌 Requirements

- Python 3.8+
- `groq`, `langchain`, `chromadb`, `streamlit`
- A valid [Groq API key](https://console.groq.com/)

---

## 📃 License

MIT License — Feel free to modify, adapt, and build upon this project.

---

## 🙋‍♂️ Contact

Made with ❤️ by [Your Name]  
📫 LinkedIn: [https://linkedin.com/in/yourname](https://linkedin.com/in/yourname)  
💻 GitHub: [https://github.com/yourusername](https://github.com/yourusername)
