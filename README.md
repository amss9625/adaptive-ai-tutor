# 🧠 Adaptive AI Tutor (v0.1)

An experimental, modular learning system designed to teach **how to think**, not how to copy answers.

This project explores adaptive instruction by analyzing user behavior, logic patterns, and conceptual misunderstandings rather than relying on correctness alone.

---

## Overview

Adaptive AI Tutor is a research-oriented tutoring framework that:

- Challenges users instead of spoon-feeding answers
- Analyzes *how* a user approaches a problem
- Detects conceptual gaps in understanding
- Injects targeted micro-lessons when needed
- Collects baseline learning data before introducing visual progress indicators

This repository represents **version 0.1**, focused on core architecture and data collection.

---

## Design Philosophy

- **Challenge over convenience**  
  Users are guided, not answered for.

- **Behavior-aware learning**  
  Time spent, hints used, and inefficient attempts influence guidance.

- **Concept-based feedback**  
  Incorrect answers trigger conceptual analysis, not penalties.

- **Modular by design**  
  Domains, subdomains, evaluators, and watchers are plug-in ready.

---

## Current Features

### Implemented

- Modular domain architecture (Coding domain implemented)
- Domain-specific exercise evaluation
- Logic-feature extraction (e.g., recursion base-case detection)
- Behavioral analysis (time, difficulty, attempt patterns)
- Concept gap detection
- Micro-lesson injection instead of direct answers
- Anonymous local user attempt logging

### Intentionally Excluded (for baseline data)

- Progress bars
- Mastery visuals
- User comparisons
- AI self-modifying logic

These will be introduced after sufficient real-world usage data is collected.

---

## Project Structure
adaptive-ai-tutor/
│
├── ai/
│   ├── init.py
│   ├── exercise_manager.py
│   ├── watcher.py
│   ├── progression_engine.py
│   ├── coding_evaluator.py
│   └── concept_gap_manager.py
│
├── gui/
│   └── main_gui.py
│
├── data/
│   └── coding_exercises.json
│
├── .gitignore
├── LICENSE
└── README.md

> Runtime-generated user data (`data/user_attempts.json`) is intentionally excluded from version control.

---

## How It Works

1. A user attempts an exercise
2. The evaluator checks correctness and extracts logic features
3. The watcher analyzes behavioral patterns
4. Concept gaps are detected
5. Targeted micro-lessons are provided (no direct answers)
6. The attempt is logged locally

---

## Running the Project

### Requirements
- Python 3.9+
- Windows (tested)

### Run

From the project root:

```bash
python gui/main_gui.py

Do not run the file from inside the gui/ directory directly.

Data Collection

User attempts are logged locally and include:
	•	Timestamp
	•	Exercise ID
	•	Correctness
	•	Extracted logic features
	•	Time spent

This data is used to improve adaptive guidance and identify common learning patterns.

⸻

Versioning

v0.1
	•	Core architecture complete
	•	Single domain implemented
	•	Baseline data collection enabled
	•	No visual progress indicators

⸻

Roadmap (High-Level)
	•	Domain and subdomain expansion
	•	Progress visualization (A/B tested)
	•	Learner clustering
	•	Expanded evaluators (trades, security, math)
	•	Packaging for non-technical users

⸻

Purpose

This project is an experiment in teaching reasoning rather than answers.

Friction is intentional.
