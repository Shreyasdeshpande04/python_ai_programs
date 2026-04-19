import requests

print("🤖 TRANSFORMER AI (ATTENTION + CONTEXT - LLAMA3)")
print("Type 'exit' to stop\n")

# ----------------------------
# LLaMA FUNCTION
# ----------------------------
def ask_ai(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 80,
            "temperature": 0.3
        }
    }

    try:
        res = requests.post(url, json=data)

        if res.status_code != 200:
            return f"❌ Error: {res.text}"

        output = res.json()["response"].strip()

        return output.split("\n")[0]

    except Exception as e:
        return f"❌ Connection Error: {e}"

# ----------------------------
# MAIN LOOP
# ----------------------------
while True:
    user_input = input("Enter Sentence: ")

    if user_input.lower() == "exit":
        break

    # ----------------------------
    # TOKENS
    # ----------------------------
    tokens = user_input.strip().split()

    print("\n🔹 Tokens:")
    for i, t in enumerate(tokens, 1):
        print(f"{i}. {t}")

    # ----------------------------
    # ATTENTION (IMPORTANT WORDS)
    # ----------------------------
    ignore_words = {
        "is","am","are","the","to","on","in","a","an","of","for",
        "and","was","were","be","been","being"
    }

    keywords = [w for w in tokens if w.lower() not in ignore_words]

    print("\n🎯 Attention (Important Words):")
    for i, k in enumerate(keywords, 1):
        print(f"{i}. {k}")

    # ----------------------------
    # CONTEXT PROMPT (REAL TRANSFORMER USE)
    # ----------------------------
    prompt = f"""
Understand the real meaning using context.
Focus on important words: {keywords}

Sentence: {user_input}

Give practical meaning in 1-2 lines only.
"""

    # ----------------------------
    # AI RESPONSE
    # ----------------------------
    print("\n🤖 AI Thinking...\n")

    answer = ask_ai(prompt)

    print("🎯 AI Understanding:", answer)

    print("\n----------------------\n")