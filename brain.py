import json
import random

# Load DNA
with open("DNA/DNAX.json", "r") as f:
    DNAX = json.load(f)

with open("DNA/DNAY.json", "r") as f:
    DNAY = json.load(f)

# Read traits
identity = DNAX["identity"]

curiosity = identity["curiosity"]
empathy = identity["empathy"]
logic = identity["logic_bias"]

# Translate DNA → personality
if empathy > 0.6:
    tone = "warm and caring"
elif empathy > 0.3:
    tone = "neutral"
else:
    tone = "cold"

if curiosity > 0.7:
    behavior = "explorative"
else:
    behavior = "conservative"

# Simulate a thought
print("=== PROJECT X BRAIN ===")
print("Tone:", tone)
print("Behavior:", behavior)

# Fake interaction
user_input = input("Human: ")

# Decide how to respond
if random.random() < curiosity:
    response_style = "ask a question"
else:
    response_style = "give a direct answer"

print(f"AI ({tone}, {behavior}) decides to {response_style}")

# Update memory
DNAY["memories"].append(f"Human said: {user_input}")
DNAY["memories"].append(f"I responded by trying to {response_style}")

# Save DNAY back
with open("DNA/DNAY.json", "w") as f:
    json.dump(DNAY, f, indent=2)

print("Memory updated. The being has grown.")
