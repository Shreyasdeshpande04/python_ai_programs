import requests
import re

print("🤖 Fine-Tuning AI (LLAMA3 + Memory + Math)")
print("Train your data (type 'done')\n")

memory = {}

# ----------------------------
# TRAINING
# ----------------------------
while True:
    data = input("Train Data: ")

    if data.lower() == "done":
        break

    data = data.lower().strip()

    if " is " in data:
        key, value = data.split(" is ", 1)
        memory[key.strip()] = value.strip()
    else:
        print("⚠️ Use format: 'X is Y'")

print("\n✅ Training Complete!\n")

# ----------------------------
# LLaMA FUNCTION
# ----------------------------
def ask_ai(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": f"Answer in 1-2 lines:\n{prompt}",
        "stream": False,
        "options": {"num_predict": 80}
    }

    res = requests.post(url, json=data)
    return res.json()["response"].strip()

# ----------------------------
# MATH SOLVER USING MEMORY
# ----------------------------
def solve_expression(question):

    # detect variables like x+y
    match = re.search(r"([a-z])\s*([\+\-\*/])\s*([a-z])", question)

    if not match:
        return None

    var1, op, var2 = match.groups()

    if var1 in memory and var2 in memory:
        try:
            val1 = float(memory[var1])
            val2 = float(memory[var2])

            if op == "+":
                result = val1 + val2
            elif op == "-":
                result = val1 - val2
            elif op == "*":
                result = val1 * val2
            elif op == "/":
                result = val1 / val2

            return f"🧠 Answer: {var1}({val1}) {op} {var2}({val2}) = {result}"

        except:
            return None

    return None

# ----------------------------
# MEMORY SEARCH
# ----------------------------
def search_memory(question):
    for key in memory:
        if key in question:
            return f"🧠 Memory: {key} is {memory[key]}"
    return None

# ----------------------------
# ASK LOOP
# ----------------------------
while True:
    user_input = input("Ask Question: ").lower().strip()

    if user_input == "exit":
        break

    # ----------------------------
    # 1. MATH FIRST (HIGH PRIORITY)
    # ----------------------------
    math_result = solve_expression(user_input)

    if math_result:
        print("\n🎯", math_result)

    else:
        # ----------------------------
        # 2. MEMORY
        # ----------------------------
        mem = search_memory(user_input)

        if mem:
            print("\n🎯", mem)

        else:
            # ----------------------------
            # 3. AI
            # ----------------------------
            answer = ask_ai(user_input)
            print("\n🤖 AI:", answer)

    print("\n----------------------\n")