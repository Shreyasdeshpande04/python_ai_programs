import requests

print("🤖 ADVANCED AI SYSTEM (LLAMA3)")

def ask_ai(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",   # ✅ FIXED
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data)

        # safety check
        if response.status_code != 200:
            return f"❌ Error: {response.text}"

        return response.json()["response"]

    except Exception as e:
        return f"❌ Connection Error: {e}"


while True:
    q = input("\nEnter Prompt: ")

    if q.lower() == "exit":
        break

    print("\n🤖 AI Thinking...\n")

    answer = ask_ai(q)

    print("🎯 Answer:")
    print(answer)

    print("\n----------------------")