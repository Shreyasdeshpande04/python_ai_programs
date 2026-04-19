import requests

print("🤖 TOKENS + LLM SYSTEM (LLAMA3)")
print("Type 'exit' to stop\n")

# ----------------------------
# LLaMA FUNCTION
# ----------------------------
def ask_ai(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": f"Answer clearly in 1-2 lines:\n{prompt}",
        "stream": False,
        "options": {
            "num_predict": 100,
            "temperature": 0.3
        }
    }

    try:
        res = requests.post(url, json=data)

        if res.status_code != 200:
            return f"❌ Error: {res.text}"

        return res.json()["response"].strip()

    except Exception as e:
        return f"❌ Connection Error: {e}"

# ----------------------------
# MAIN LOOP
# ----------------------------
while True:
    user_input = input("Enter Prompt: ")

    if user_input.lower() == "exit":
        break

    # ----------------------------
    # TOKENS (WORD LEVEL)
    # ----------------------------
    tokens = user_input.strip().split()

    print("\n🔹 Tokens:")
    for i, t in enumerate(tokens, 1):
        print(f"{i}. {t}")

    print(f"\n🔢 Total Tokens: {len(tokens)}")

    # ----------------------------
    # CHARACTER TOKENS (ADVANCED)
    # ----------------------------
    char_tokens = list(user_input)

    print(f"🔤 Character Tokens: {len(char_tokens)}")

    # ----------------------------
    # AI RESPONSE
    # ----------------------------
    print("\n🤖 AI Thinking...\n")

    answer = ask_ai(user_input)

    # clean first line
    answer = answer.split("\n")[0]

    print("🎯 AI Response:", answer)

    print("\n----------------------\n")