# 📘 🤖 AI SYSTEM – SETUP & RUN GUIDE

## 🔹 1. Requirements

```bash
Python 3.10+
```

Check:

```bash
python --version
```

---

# 🧠 Part 1: Run AI Programs (Ollama Required)

These programs use a **local LLM via Ollama**

## 🔹 Install Dependencies

```bash
pip install transformers torch requests
```

## 🔹 Install & Setup Ollama

👉 [https://ollama.com](https://ollama.com)

```bash
ollama pull llama3
```

```bash
ollama run llama3
```

---

## 🔹 Run Programs

```bash
python dataset.py
python agents.py
python transformer.py
```

📌 Refer screenshots for output

---

# 🚀 Part 2: AI Data Analyst Project

## 🔹 Open in VS Code

* Open: `ai-data-analyst-project`
* Open terminal

---

## 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 Setup Environment Variable

In `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 🔹 Run Project

```bash
uvicorn app.main:app --reload
```

---

## 🔹 Open in Browser

```
http://127.0.0.1:8000
```

Docs:

```
http://127.0.0.1:8000/docs
```

---