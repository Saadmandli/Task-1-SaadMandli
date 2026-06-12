# 🤖 Rule-Based AI Chatbot
### DecodeLabs Industrial Training | Batch 2026 | Project 1 — AI Track

---

## 📌 Project Overview

A **Rule-Based AI Chatbot** built in Python that simulates basic human interaction through pure programmatic decision-making. This project demonstrates the fundamentals of **Control Flow**, **Input Sanitization**, and **Dictionary-based Intent Matching** — the building blocks of intelligent systems.

> *"An LLM without rules is a hallucination engine. Today, we build the skeleton that holds the intelligence."*
> — DecodeLabs Architecture Briefing

---

## 🗂️ Project Structure

```
Task-1-SaadMandli/
│
├── chatbot.py          # Main chatbot engine (IPO loop)
├── responses.py        # Knowledge base — all predefined responses
└── README.md           # Project documentation
```

---

## ⚙️ How It Works — The IPO Model

The chatbot follows a 3-phase architecture:

```
INPUT  ──────►  PROCESS  ──────►  OUTPUT
(Raw Feed)    (Logic Skeleton)  (Feedback Loop)
Sanitization   Intent Matching   Response
& Normalization  & State          Generation
```

### Phase 1 — Input & Sanitization
Raw user input is cleaned using `.lower().strip()` so that `"Hello"`, `"HELLO"`, and `"  hello  "` all resolve to `"hello"`.

### Phase 2 — Intent Matching (Dictionary Lookup)
Instead of an if-elif ladder (O(n)), the chatbot uses a **Python dictionary** for O(1) constant-time lookups. All responses are stored in `responses.py` and imported into the main engine.

### Phase 3 — Output & Fallback
If the input matches a key in the knowledge base, the mapped response is returned. If not, a default fallback message is displayed.

---

## 🧠 Key Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Input Sanitization | `.lower().strip()` on every input |
| Continuous Loop | `while True` loop as the chatbot heartbeat |
| Knowledge Base | Dictionary in `responses.py` with 5+ intents |
| O(1) Lookup | `responses.get(user_input, fallback)` |
| Exit Strategy | `"quit"` / `"exit"` triggers a clean `break` |
| Fallback Response | Default reply for unrecognized inputs |

---

## 🚀 How to Run

**Prerequisites:** Python 3.x installed

```bash
# Clone the repository
git clone https://github.com/Saadmandli/Task-1-SaadMandli.git

# Navigate into the project folder
cd Task-1-SaadMandli

# Run the chatbot
python chatbot.py
```

---

## 💬 Sample Interaction

```
==============================
   DecodeLabs AI Chatbot 🤖
   Type 'quit' to exit
==============================

You: hello
Bot: Hi there! How can I help you today?

You: what is your name
Bot: I'm DecoBot, your rule-based assistant!

You: how are you
Bot: I'm running at 100% efficiency. All systems nominal!

You: bye
Bot: Goodbye! Have a great day!

You: quit
Bot: Shutting down... See you next time!
```

---

## 📁 responses.py — Knowledge Base

All chatbot responses are stored in a separate `responses.py` file as a Python dictionary, following the **O(1) Hash Map pattern** taught in the project briefing.

```python
# responses.py

RESPONSES = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hey! Great to see you.",
    "how are you": "I'm running at 100% efficiency. All systems nominal!",
    "what is your name": "I'm DecoBot, your rule-based assistant!",
    "bye": "Goodbye! Have a great day!",
    "quit": "Shutting down... See you next time!",
    # Add more intents below ⬇️
}

FALLBACK = "I do not understand that yet. Try rephrasing!"
```

---

## 🏗️ Architecture Philosophy

This project implements the **"White Box"** model of AI:

- **Traceability** — Every input maps to a known output. No mystery.
- **Safety** — Zero hallucination risk. 100% hard-coded responses.
- **Compliance** — Deterministic behavior essential for controlled environments.

This is the **control layer** — the same concept used by frameworks like NVIDIA NeMo Guardrails and Llama Guard in production AI systems.

---

## 🔧 Possible Enhancements

- Add more intents to `responses.py` to expand the bot's vocabulary
- Implement keyword-based partial matching using `in` operator
- Add a conversation logger to save chat history
- Give the bot a unique personality with varied responses using `random.choice()`
- Build a simple GUI using `tkinter`

---

## 👨‍💻 Author

**Saad Mandli**

---

## 🏢 About DecodeLabs

> *Powered by DecodeLabs | Greater Lucknow, India*
> 📧 decodelabs.tech@gmail.com | 🌐 www.decodelabs.tech
