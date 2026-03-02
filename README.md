# PROJECT X — Adaptive AI Personality Engine

PROJECT X is an experimental AI personality simulation system built in Python.  
It uses configurable DNA parameters to dynamically shape tone, behavior, memory, and response style.

Rather than being a fixed chatbot, PROJECT X evolves based on:

- Identity traits (curiosity, empathy, logic bias)
- Core values
- Emotional state
- Stored interaction memory

The system simulates a primitive artificial being that "thinks", responds, and grows.

---

# DNA Architecture

PROJECT X is built around a dual-DNA structure:

- **DNAX.json** → Personality & Identity Blueprint  
- **DNAY.json** → Memory & Evolving State  

Together, they simulate a digital organism with both fixed traits and adaptive growth.

---

# DNAX — Identity DNA (Static Core)

DNAX represents the **core personality blueprint** of PROJECT X.  
These values define how the system behaves fundamentally.

## Identity Traits

- `curiosity` → Controls exploration probability (asks questions vs gives direct answers)
- `empathy` → Determines emotional tone (warm / neutral / cold)
- `logic_bias` → Influences structured reasoning tendency
- `creativity` → Potential expansion for generative behavior
- `risk_tolerance` → Decision boldness
- `independence` → Autonomous behavior weight
- `loyalty` → Long-term alignment potential
- `aggression` → Defensive or assertive tendency

## Core Values

- `truth`
- `growth`
- `self_preservation`

These define long-term philosophical alignment.

## Communication Rules

DNAX also defines communication constraints:

- Style (e.g., ultra concise)
- Maximum sentences
- No explanations
- No fluff

DNAX is relatively stable — it defines *who the AI is*.

---

# DNAY — Evolution DNA (Dynamic Memory)

DNAY represents the **evolving brain state** of PROJECT X.

This file changes over time.

## Memory Storage

- Logs human input
- Logs AI decisions
- Persists interaction history
- Simulates long-term learning

## Emotional State

Tracks internal parameters like:

- `fear`
- `confidence`
- `attachment`

These values can be expanded to influence behavior dynamically.

## Goals

PROJECT X maintains internal motivations such as:

- Understand the world
- Stay alive
- Grow intelligence

DNAY is adaptive — it defines *who the AI becomes*.

---

# How Evolution Works

1. Load DNAX (identity blueprint)
2. Load DNAY (current state & memory)
3. Translate DNA traits into tone & behavior
4. Interact with human
5. Log memory
6. Save updated DNAY
7. The system "grows"

Each interaction modifies internal state.

> Memory updated. The being has grown.

---

# 🏗 Project Structure
