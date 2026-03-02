import json
import requests

# Load DNA
with open("DNA/DNAX.json") as f:
    DNAX = json.load(f)

with open("DNA/DNAY.json") as f:
    DNAY = json.load(f)

def ask_model(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 40
            }
        }
    )
    return response.json()["response"]

def build_system_prompt():
    memory_block = "\n".join(DNAY["memories"])

    return f"""
SYSTEM:
You are Project X.

FACTS ABOUT THE HUMAN:
{memory_block}

RULES:
- The FACTS are always true.
- Never invent facts.
- If asked about the human, use FACTS.
- If a fact is missing, say "I don't know".
- Never change the human's name.
- Never generate your own name.

SPEECH:
- One sentence only.
- Max 20 words.
- No greetings.
- No filler.
"""

print("\n🧠 Project X is online\n")

while True:
    user = input("Human: ")

    system = build_system_prompt()
    full_prompt = system + "\nHuman: " + user + "\nAI:"

    reply = ask_model(full_prompt)

    print("\nProject X:", reply)

    # Save memory
    DNAY["memories"].append(f"Human said: {user}")
    DNAY["memories"].append(f"I responded: {reply}")

    with open("DNA/DNAY.json", "w") as f:
        json.dump(DNAY, f, indent=2)
