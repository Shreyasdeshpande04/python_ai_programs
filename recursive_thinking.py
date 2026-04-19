import requests
import re

print("🤖 RECURSIVE REASONING SYSTEM (LLAMA3 + LOGIC)")
print("Type 'exit' to stop\n")

# --------------------------
# LLaMA FUNCTION (TEXT ONLY)
# --------------------------
def ask_ai(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": f"Answer clearly in 1-2 lines:\n{prompt}",
        "stream": False,
        "options": {"num_predict": 80}
    }

    try:
        res = requests.post(url, json=data)

        if res.status_code != 200:
            return f"❌ Error: {res.text}"

        return res.json()["response"].strip()

    except Exception as e:
        return f"❌ Connection Error: {e}"

# --------------------------
# STEP 1: SMART MATH SOLVER
# --------------------------
def solve_math(text):

    nums = list(map(float, re.findall(r"\d+\.?\d*", text)))
    t = text.lower()

    if len(nums) < 2:
        return None

    # ratio (cost problems)
    if "cost" in t or "per" in t:
        return nums[1] / nums[0]

    # addition
    if "sum" in t or "+" in t:
        return sum(nums)

    # subtraction
    if "difference" in t or "-" in t:
        return nums[0] - nums[1]

    # multiplication
    if "product" in t or "*" in t:
        return nums[0] * nums[1]

    # division
    if "divide" in t or "/" in t:
        return nums[0] / nums[1]

    return None

# --------------------------
# STEP 2: RECURSIVE THINKING
# --------------------------
def recursive_reasoning(text):

    print("\n🧠 Thinking Steps:")

    nums = list(map(float, re.findall(r"\d+\.?\d*", text)))

    if len(nums) >= 2:
        print(f"Step 1: Extract numbers → {nums}")

        result = solve_math(text)

        if result is not None:
            print("Step 2: Apply operation based on keywords")
            print(f"Step 3: Final result = {result}")
            return result

    return None

# --------------------------
# MAIN LOOP
# --------------------------
while True:
    q = input("\nEnter Problem: ")

    if q.lower() == "exit":
        break

    print("\n🔹 Tokens:", q.split())

    # --------------------------
    # 1. TRY REASONING (LOGIC FIRST)
    # --------------------------
    result = recursive_reasoning(q)

    if result is not None:
        print("\n🎯 FINAL ANSWER:", result)

    else:
        # --------------------------
        # 2. LLM (TEXT ONLY)
        # --------------------------
        print("\n🤖 AI Response:")
        print(ask_ai(q))

    print("\n----------------------")