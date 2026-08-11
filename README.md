# 🤖 ShrikAi — Personal AI Assistant & Interactive HR Portfolio

**ShrikAi** is a state-of-the-art, interactive personal AI assistant built for **Srikantha**. Designed with a stunning, high-converting HR-focused interface, ShrikAi acts as a 24/7 digital ambassador that answers recruiters' and hiring managers' questions about Srikantha's skills, work experience, key projects, and workplace culture.

features-Hr can ask question related to my skills ,weakness,etc
Ai will answer the question.

Note:More Unique Fetures will coming soon.

## 🏗️ Architecture & Tech Stack

- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism, CSS Grid/Flexbox, Dynamic SVG icons, Custom Animations), JavaScript (Fetch API, LocalStorage persistence).
- **Typography**: [Google Fonts — Outfit](https://fonts.google.com/specimen/Outfit)
- **Backend Framework**: Python 3.10+, FastAPI, Pydantic v2, Uvicorn
- **AI / LLM Engine**: Google GenAI SDK (`google-genai`), Gemini 3.5 Flash Lite Model
- **Document Processing**: `pypdf` for PDF parsing

---

## 📁 Repository Structure

```
personal ai/
├── frontend/
│   ├── index.html          # Main web application & HR chat interface
│   └── profile.jpg         # Default profile picture for Srikantha
├── src/
│   ├── main.py             # FastAPI entry point & lifespan data manager
│   ├── core/               # App configuration & FastAPI dependency injection
│   │   ├── config.py
│   │   └── dependencies.py
│   ├── document/           # Input documents (Resume PDF & Personal Profile)
│   │   ├── personal-doc.pdf
│   │   └── personal-doc.txt
│   ├── exception/          # Custom exception classes & global error handlers
│   ├── routers/            # API endpoints (/chat/)
│   ├── schema/             # Pydantic validation models
│   ├── services/           # PDF extraction & Gemini LLM completion services
│   └── systemprompt/       # ShrikAi system prompts & instructions
├── .env                    # Environment variables (API Keys)
├── requirment.txt          # Python project dependencies
└── README.md               # Documentation
```

---

## 🚀 Quick Start & Installation

### 1. Prerequisites
- Python 3.10 or higher installed on your system.
- A **Google Gemini API Key** (obtainable from [Google AI Studio](https://aistudio.google.com/)).

### 2. Configure Environment
Create a `.env` file in the root directory:
```env
LLM_API_KEY=your_gemini_api_key_here
```

### 3. Install Dependencies
Set up a virtual environment and install required packages:
```bash
python -m venv .venv
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1

pip install -r requirment.txt
```

### 4. Run the Server
Launch the FastAPI development server:
```bash
python -m uvicorn src.main:app --reload --port 8000
```

### 5. Access ShrikAi
Open your browser and navigate to:
👉 **`http://127.0.0.1:8000`**

---


## 📄 License & Credits

Designed & Developed by **Srikantha** — Powered by FastAPI & Gemini.
