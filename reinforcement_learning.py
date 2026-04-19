import requests

print("🤖 RLHF SYSTEM (LLAMA3 + SMART LEARNING)")
print("Train first → then ask")
print("Type 'exit' anytime\n")

# ----------------------------
# TRAINING DATASET
# ----------------------------
dataset = []

while True:
    data = input("Train Data: ")

    if data.lower() == "done":
        break

    dataset.append(data.lower().strip())

print("\n✅ Training Complete!\n")

# ----------------------------
# MEMORY (RLHF)
# ----------------------------
memory = {}

# ----------------------------
# LLaMA FUNCTION
# ----------------------------
def ask_ai(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": f"Answer in 1 line only:\n{prompt}",
        "stream": False,
        "options": {"num_predict": 60}
    }

    try:
        res = requests.post(url, json=data)

        if res.status_code != 200:
            return f"❌ Error: {res.text}"

        return res.json()["response"].strip().split("\n")[0]

    except Exception as e:
        return f"❌ Connection Error: {e}"

# ----------------------------
# SMART FILTER (IMPROVED)
# ----------------------------
def smart_answer(q):

    q = q.lower()

    # like
    if "like" in q and "dont" not in q:
        for d in dataset:
            if "like" in d and "dont" not in d:
                return d

    # dont like
    if "dont like" in q:
        for d in dataset:
            if "dont like" in d:
                return d

    # location
    if "where" in q or "live" in q or "am" in q:
        for d in dataset:
            if "in" in d:
                return d

    return None

# ----------------------------
# MAIN LOOP (RLHF)
# ----------------------------
while True:
    user_input = input("Ask Question: ").lower().strip()

    if user_input == "exit":
        break

    # ----------------------------
    # 1. MEMORY (LEARNED)
    # ----------------------------
    if user_input in memory:
        print("\n🎯 Learned Response:", memory[user_input])
        print("\n----------------------\n")
        continue

    # ----------------------------
    # 2. SMART FILTER
    # ----------------------------
    answer = smart_answer(user_input)

    # ----------------------------
    # 3. LLaMA (FALLBACK)
    # ----------------------------
    if not answer:
        answer = ask_ai(user_input)

    print("\n🤖 AI Response:", answer)

    # ----------------------------
    # 4. RLHF FEEDBACK
    # ----------------------------
    feedback = input("Feedback (👍 / 👎): ")

    if feedback == "👍":
        memory[user_input] = answer
        print("✅ Learned")

    else:
        correct = input("👉 Enter correct answer: ")
        memory[user_input] = correct
        print("✅ Updated with correct answer")

    print("\n----------------------\n")