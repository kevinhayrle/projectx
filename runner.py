import json
import subprocess

# Load DNA
with open("DNA/DNAX.json") as f:
    DNAX = json.load(f)

with open("DNA/DNAY.json") as f:
    DNAY = json.load(f)

def ask_mistral(prompt):
    process = subprocess.Popen(
        ["ollama", "run", "mistral"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )
    out, err = process.communicate(prompt)
    return out.strip()

def build_system_prompt():
    memory_block = "\n".join(DNAY["memories"])

    return f"""
You are Project X.

Your internal identity:
{json.dumps(DNAX["identity"], indent=2)}

Your core values:
{json.dumps(DNAX["core_values"], indent=2)}

Your memory:
{memory_block}

You must behave according to this memory and identity.
If the human asks about their name, use memory.
"""

print("\n🧠 Project X is online\n")

while True:
    user = input("Human: ")

    system = build_system_prompt()
    full_prompt = system + "\nHuman: " + user + "\nAI:"

    reply = ask_mistral(full_prompt)

    print("\nProject X:", reply)

    # Save conversation to memory
    DNAY["memories"].append(f"Human said: {user}")
    DNAY["memories"].append(f"I responded: {reply}")

    with open("DNA/DNAY.json", "w") as f:
        json.dump(DNAY, f, indent=2)
