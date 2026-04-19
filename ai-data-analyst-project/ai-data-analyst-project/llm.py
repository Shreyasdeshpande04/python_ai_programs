import requests

print("🤖 LLM SYSTEM (LLAMA3 - SMART Q&A)")
print("Type 'exit' to stop\n")

# ----------------------------
# LLaMA FUNCTION
# ----------------------------
def ask_ai(question):

    url = "http://localhost:11434/api/generate"

    prompt = f"""
Answer the question in one clear sentence.
Do not repeat the question.
Do not add extra explanation.

Question: {question}
Answer:
"""

    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 60,
            "temperature": 0.3
        }
    }

    try:
        res = requests.post(url, json=data)

        if res.status_code != 200:
            return f"❌ Error: {res.text}"

        output = res.json()["response"].strip()

        # clean extra lines
        answer = output.split("\n")[0]

        return answer

    except Exception as e:
        return f"❌ Connection Error: {e}"

# ----------------------------
# MAIN LOOP
# ----------------------------
while True:
    question = input("Enter Question: ")

    if question.lower() == "exit":
        break

    print("\n🤖 Thinking...\n")

    answer = ask_ai(question)

    print("🎯 Answer:", answer)

    print("\n----------------------\n")