# TeachTrace AI — AI-Powered Classroom Intelligence & Learning Gap System

> *"Don't just trace the marks. Trace the learning gap."*

TeachTrace AI is an AI-powered classroom intelligence platform that transforms student answers into actionable teaching decisions. By combining Retrieval-Augmented Generation (RAG) and linguistic analysis, it diagnoses *why* students struggle rather than simply showing *who* got low marks.

## 🚀 Key Features

1. **RAG & Linguistic Analysis**: Analyzes student answers across grammar, vocabulary, reasoning logic, and conceptual understanding.
2. **Learning Gap Map**: Central dashboard displaying top class-wide misconceptions, affected student counts, and severity tiers.
3. **Question Ambiguity Detector**: Flags unclear test questions that cause widespread student misinterpretation.
4. **Targeted Intervention Generator**: Automatically creates 15-minute reteaching plans and student sorting/explanation activities.
5. **Reassessment & Improvement Metrics**: Generates 3-question follow-up checks and compares before vs. after class performance.

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **LLM Engine:** Groq API (Llama 3.3 70B) / Gemini API
- **RAG & Vector DB:** LangChain / ChromaDB
- **Data Processing:** Pandas / PyPDF

## 📦 Local Installation & Setup

1. **Clone & Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Secrets:**
   Create `.streamlit/secrets.toml` with your Groq API key:
   ```toml
   GROQ_API_KEY = "gsk_your_key_here"
   ```

3. **Run Streamlit App:**
   ```bash
   streamlit run app.py
   ```

---
*Developed for Pak Angels GenAI Cohort 11 Mid-Program Hackathon.*
