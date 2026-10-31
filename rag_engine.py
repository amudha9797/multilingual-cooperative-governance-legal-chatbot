import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")


def get_fallback_answer(query):
    # Match against data.json for relevant answer
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                query_words = set(query.lower().split())
                best_match = None
                best_overlap = 0
                for item in data:
                    q = item.get("question", "").lower()
                    overlap = len(query_words.intersection(set(q.split())))
                    if overlap > best_overlap:
                        best_overlap = overlap
                        best_match = item.get("answer", "")
                if best_match and best_overlap >= 1:
                    return best_match
        except Exception:
            pass
    return (
        "Cooperative Society Legal & Governance Information: Guidance on Primary Agricultural Cooperative Credit Societies (PACS), "
        "Tamil Nadu Cooperative Societies Act 1983 and Rules 1988, KCC Loan (4% interest), and PMFBY Crop Insurance."
    )


def query_legal_rag(user_query, language="English", api_key=None):
    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY", "").strip()

    if api_key and api_key.strip():
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"""
You are an expert AI Legal & Governance Assistant specializing in Indian Cooperative Societies, particularly the Tamil Nadu Cooperative Societies Act 1983 and Tamil Nadu Cooperative Societies Rules 1988.
You provide accurate, legally compliant, and easy-to-understand assistance for cooperative members, PACS, farmers, and administrators.

User Language: {language}
User Question: {user_query}

Instructions:
1. Respond completely and fluently in {language}.
2. Provide precise, legally accurate information referencing cooperative principles, PACS, membership rights, loan procedures, or relevant sections of the Tamil Nadu Cooperative Societies Act 1983/Rules 1988 when applicable.
3. Keep the explanation clear, professional, and accessible.
"""
            resp = model.generate_content(prompt)
            if resp and resp.text:
                return resp.text.strip()
        except Exception as e:
            print("Gemini API error in query_legal_rag:", e)

    return get_fallback_answer(user_query)
