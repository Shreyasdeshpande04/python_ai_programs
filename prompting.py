import requests

print("🤖 Prompting AI (LLAMA3 - Smart Prompting)")
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
            "num_predict": 100,
            "temperature": 0.3
        }
    }

    try:
        res = requests.post(url, json=data)

        if res.status_code != 200:
            return f"❌ Error: {res.text}"

        output = res.json()["response"].strip()

        # clean first line only
        return output.split("\n")[0]

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
    # Detect Prompt Type
    # ----------------------------
    if len(user_input.split()) <= 2:
        prompt_type = "Simple Prompt"
    elif "act as" in user_input.lower():
        prompt_type = "Role-Based Prompt"
    elif "explain" in user_input.lower() or "write" in user_input.lower():
        prompt_type = "Instruction-Based Prompt"
    else:
        prompt_type = "Detailed Prompt"

    print(f"\n🧠 Detected Type: {prompt_type}")

    # ----------------------------
    # Tokenization
    # ----------------------------
    tokens = user_input.split()

    print("\n🔹 Tokens:")
    for i, t in enumerate(tokens, 1):
        print(f"{i}. {t}")

    # ----------------------------
    # SMART PROMPT ENGINEERING
    # ----------------------------
    if prompt_type == "Simple Prompt":
        final_prompt = f"Answer in 1 line: {user_input}"

    elif prompt_type == "Role-Based Prompt":
        final_prompt = f"{user_input}\nGive a professional answer in 2 lines."

    elif prompt_type == "Instruction-Based Prompt":
        final_prompt = f"{user_input}\nExplain clearly in 2-3 lines."

    else:
        final_prompt = f"Answer clearly and correctly in short:\n{user_input}"

    # ----------------------------
    # AI RESPONSE
    # ----------------------------
    print("\n🤖 AI Thinking...\n")

    answer = ask_ai(final_prompt)

    print("🎯 AI Response:", answer)

    print("\n----------------------\n")