import re
import ast
import operator

print("🤖 SMART AGENT SYSTEM (ADVANCED + SAFE)")
print("Type 'exit' to stop\n")

# -------------------------
# SAFE CALCULATOR (NO eval)
# -------------------------
ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def safe_eval(expr):
    try:
        node = ast.parse(expr, mode='eval').body

        def calc(n):
            if isinstance(n, ast.Num):
                return n.n
            elif isinstance(n, ast.BinOp):
                return ops[type(n.op)](calc(n.left), calc(n.right))
            else:
                raise Exception("Invalid")

        return calc(node)
    except:
        return None

# -------------------------
# ALGEBRA
# -------------------------
def solve_algebra(text):
    pattern = r"([a-z])\+([a-z])\s*=?\s*(\d+).*([a-z])\s*=?\s*(\d+)"
    m = re.search(pattern, text.replace(" ", "").lower())

    if m:
        v1, v2, total, known_v, known_val = m.groups()
        total = int(total)
        known_val = int(known_val)

        if v1 == known_v:
            return f"🧠 Answer: {v2} = {total - known_val}"
        if v2 == known_v:
            return f"🧠 Answer: {v1} = {total - known_val}"

    return None

# -------------------------
# EVEN / ODD
# -------------------------
def even_odd(text):
    if "even" in text or "odd" in text:
        nums = re.findall(r"\d+", text)
        if nums:
            n = int(nums[0])
            return f"🧠 Answer: {n} is {'EVEN' if n%2==0 else 'ODD'}"
    return None

# -------------------------
# PRIME
# -------------------------
def prime(text):
    if "prime" in text:
        nums = re.findall(r"\d+", text)
        if nums:
            n = int(nums[0])

            if n <= 1:
                return f"🧠 Answer: {n} is NOT PRIME"

            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return f"🧠 Answer: {n} is NOT PRIME"

            return f"🧠 Answer: {n} is PRIME"
    return None

# -------------------------
# CALCULATOR
# -------------------------
def calculator(text):
    expr = re.findall(r"[0-9\+\-\*/\.]+", text)
    if expr:
        result = safe_eval(expr[0])
        if result is not None:
            return f"🧠 Answer: {result}"
    return None

# -------------------------
# TEXT UNDERSTANDING
# -------------------------
def text_response(text):
    t = text.lower()

    if "how are you" in t:
        return "🧠 Answer: I am fine"

    if "your name" in t:
        return "🧠 Answer: I am an AI agent"

    if "i am" in t:
        return f"🧠 Noted: {text}"

    return None

# -------------------------
# FALLBACK (SMART DEFAULT)
# -------------------------
def fallback(text):
    return "🤖 I understand your input, but I need more logic/training to answer accurately."

# -------------------------
# AGENT (BRAIN)
# -------------------------
def agent(task):

    t = task.lower()

    print("\n🧠 Agent Routing...")

    # priority-based routing
    for tool in [solve_algebra, even_odd, prime, calculator, text_response]:
        result = tool(t)
        if result:
            return result

    return fallback(task)

# -------------------------
# MAIN LOOP
# -------------------------
while True:
    task = input("\nEnter Task: ")

    if task.lower() == "exit":
        break

    print("\n🔎 Thinking...")
    print("\n🎯 Final Output:")
    print(agent(task))

    print("\n----------------------")