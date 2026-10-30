# Multilingual Cooperative Governance & Legal Chatbot

An AI-powered multilingual chatbot for cooperative governance and legal assistance based on the Tamil Nadu Cooperative Societies Act 1983 and Rules 1988.

---

## 🌟 Features

- **Multilingual Support**: Supports inquiries in multiple languages including English, Tamil, and more.
- **Legal & Governance Intelligence**: Built around Tamil Nadu Cooperative Societies Act 1983 and Rules 1988.
- **RAG & Fallback Engine**: Integrates Google Gemini AI for smart queries with local database fallback.
- **Voice Support**: Speech-to-text (STT) and text-to-speech (TTS) powered by Sarvam AI.
- **Admin Dashboard**: Manage cooperative knowledge base, view enquiries, and configure legal Q&A entries.

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/amudha9797/multilingual-cooperative-governance-legal-chatbot.git
cd multilingual-cooperative-governance-legal-chatbot
```

### 2. Set up virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Configure Environment Variables
Create a `.env` file in the root directory for voice and advanced AI features:
```env
SARVAM_API_KEY=your_sarvam_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### 5. Run the application
```bash
python app.py
```

Access the application in your browser:
- **Chatbot Interface**: `http://127.0.0.1:5000/`
- **Admin Panel**: `http://127.0.0.1:5000/admin/login`
