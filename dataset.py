import requests

print("📊 DATASET + AI LEARNING SYSTEM (LLAMA3)")
print("Type 'done' to stop\n")

# ----------------------------
# STEP 1: DATA COLLECTION
# ----------------------------
dataset = []

while True:
    data = input("Enter data: ")

    if data.lower() == "done":
        break

    dataset.append(data)

# ----------------------------
# STEP 2: SHOW RAW DATA
# ----------------------------
print("\n🔹 Raw Dataset:")
print(dataset)

# ----------------------------
# STEP 3: CLEANING
# ----------------------------
cleaned_data = []

for item in dataset:
    item = item.strip().lower()

    if item != "" and item not in cleaned_data:
        cleaned_data.append(item)

# ----------------------------
# STEP 4: SHOW CLEAN DATA
# ----------------------------
print("\n🔹 Cleaned Dataset:")
for i, data in enumerate(cleaned_data, 1):
    print(f"{i}. {data}")

print("\n📊 Dataset Size:", len(cleaned_data))

# ----------------------------
# STEP 5: REPEAT LOGIC (100% CORRECT)
# ----------------------------
def find_repeats(data):
    freq = {}
    for item in data:
        item = item.lower().strip()
        freq[item] = freq.get(item, 0) + 1

    repeats = [k for k, v in freq.items() if v > 1]

    if repeats:
        return "🧠 Repeated: " + ", ".join(repeats)
    else:
        return "🧠 No repetition found"

# ----------------------------
# STEP 6: AI FUNCTION (LLAMA)
# ----------------------------
def ask_ai(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": f"Answer in 1-2 lines only:\n{prompt}",
        "stream": False,
        "options": {
            "num_predict": 80
        }
    }

    try:
        response = requests.post(url, json=data)

        if response.status_code != 200:
            return f"❌ Error: {response.text}"

        return response.json()["response"]

    except Exception as e:
        return f"❌ Connection Error: {e}"

# ----------------------------
# STEP 7: AI ANALYSIS
# ----------------------------
if cleaned_data:
    print("\n🤖 AI ANALYSIS...\n")

    dataset_text = ", ".join(cleaned_data)

    result = ask_ai(f"Analyze this dataset: {dataset_text}")

    print("🎯 AI Insight:")
    print(result.strip())

# ----------------------------
# STEP 8: QUESTION SYSTEM
# ----------------------------
while True:
    q = input("\nAsk about dataset (or type exit): ")

    if q.lower() == "exit":
        break

    # ✅ handle repeat using logic (not AI)
    if "repeat" in q.lower():
        print(find_repeats(dataset))
        continue

    # ✅ use raw dataset for AI
    prompt = f"Raw Dataset: {dataset}\nQuestion: {q}"

    answer = ask_ai(prompt)

    print("🤖 AI:", answer.strip())

    print("\n----------------------")