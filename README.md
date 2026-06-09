# Purple Team & Agentic AI Roadmap 🧭

**By KyberPhantasma**
**Status: Work in Progress**

---

## Overview

An interactive command-line roadmap tracker for the full Purple Team & Agentic AI learning journey — from environment setup through competitive smart contract auditing and AI agent development.

Features persistent progress tracking saved locally to `progress.json`.

Built in Python to demonstrate structured data management, file I/O, OOP design, and clean CLI architecture.

---

## Phases

| Phase | Title | Duration |
|---|---|---|
| 00 | Environment Setup | Week 1 |
| 01 | The Foundations | Months 1 – 3 |
| 02 | Web2 Hunter & AI Assistant | Months 4 – 6 |
| 03 | Web3 & Smart Contract Security | Months 7 – 10 |
| 04 | Purple Team & Agentic AI | Month 11+ |

---

## How to Run

**Requirements:** Python 3.6+ (no external libraries needed)

```bash
python main.py
```

**Example commands:**

```
ROADMAP › overview
ROADMAP › phase 0
ROADMAP › phase 3
ROADMAP › deliverables 1
ROADMAP › check 1 3
ROADMAP › resources 2
ROADMAP › all
ROADMAP › progress
ROADMAP › start
```

Progress is **automatically saved** to `progress.json` every time you check a deliverable.

---

## Project Structure

```
purple-team-roadmap/
│
├── main.py          # Entry point — interactive roadmap terminal
├── tracker.py       # Tracker class — display, progress, persistence
├── data.py          # All roadmap content (phases, deliverables, resources)
├── progress.json    # Auto-generated — your saved progress
└── README.md        # This file
```

---

## Concepts Demonstrated

- Object-Oriented Programming (classes, methods, encapsulation)
- File I/O with JSON for persistent data storage
- Separation of concerns (data / logic / interface layers)
- Dictionary and list manipulation across nested structures
- Progress calculation and visual progress bars
- Command parsing and argument handling
- Error handling for invalid input

---

## Roadmap of Features

- [ ] Add a timer/session log to track study hours per phase
- [ ] Export progress report to a Markdown or PDF file
- [ ] Add note-taking per deliverable
- [ ] Add a quiz mode for phase concepts
- [ ] Build a web dashboard version using Flask

---

## Principles

> Follow phases in order. Background Threads run continuously.
> Portfolio deliverables are non-negotiable.
> This is a marathon. Consistency beats intensity.

---

*Kybernos Labs — "We train the people who guard the world."*
