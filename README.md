# 📝 Console Todo Application — Phase I

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.13%2B-blue)
![Phase](https://img.shields.io/badge/phase-I-orange)
![Architecture](https://img.shields.io/badge/architecture-clean-success)

> **In-Memory · Python · Console · Agentic Development**

A clean, minimal **Python console-based Todo application** built as **Phase I** of a multi-phase system.  
This phase focuses on **core CRUD logic, clean architecture, and a spec-driven agentic workflow**.

---

## ✨ Why This Project Exists

This is **not** “just another Todo app.”

It is a **reference-quality Phase I implementation** designed to demonstrate:

- Spec-first development
- Agent-driven planning & implementation
- Deterministic, testable business logic
- Architecture that scales *without rewrites*

No frameworks.  
No persistence.  
No manual coding.

---

## 🧠 Agentic Development Workflow

```text
/specify  →  /plan  →  /tasks  →  Claude Code
   ↓           ↓        ↓           ↓
 Scope       Architecture  Execution   Working App
This repository represents the final output of Phase I in that workflow.

🚀 Features (Phase I)
✔ Add todos (title + description)
✔ List todos with status indicators
✔ Update todo details
✔ Mark todos as complete / incomplete
✔ Delete todos by ID

⚠️ All data is stored only in memory.
Restarting the app clears all todos — by design.

🎞️ CLI Demo (GIF-Style)
text
Copy code
▶ python src/cli/console_app.py

📝 Todo Application
──────────────────
1. Add Todo
2. List Todos
3. Update Todo
4. Mark Complete / Incomplete
5. Delete Todo
6. Exit
text
Copy code
▶ Add Todo
Title: Buy groceries
Description: Milk, eggs, bread

✅ Todo added successfully!
text
Copy code
▶ List Todos

[1] Buy groceries
    Status: ⏳ Pending
    Description: Milk, eggs, bread
text
Copy code
▶ Mark Complete

✔ Todo marked as completed!
text
Copy code
▶ List Todos

[1] Buy groceries
    Status: ✅ Completed
(Deterministic, predictable, boring — exactly how core logic should be.)

🧩 Tech Stack
Category	Choice
Language	Python 3.13+
Interface	Console / CLI
Storage	In-memory (Python data structures)
Tooling	Agentic Dev Stack, Claude Code
Style	Clean Architecture, PEP-8

⚙️ Installation
bash
Copy code
git clone <repo-url>
cd console-todo-app
python --version
No dependencies.
No configuration.
Just Python.

▶️ Usage
Run the application:

bash
Copy code
python src/cli/console_app.py
Navigate using numeric menu options and follow prompts.

🏗️ Architecture
Phase I follows a layered, framework-agnostic architecture:

text
Copy code
User Input
   ↓
Console UI (CLI)
   ↓
TodoService (Business Logic)
   ↓
TodoRepository (In-Memory Store)
   ↓
Todo Model
Architectural Guarantees
Business logic does not depend on the CLI

Storage can be swapped without refactoring logic

Deterministic execution

Phase II–ready by design

📁 Project Structure
text
Copy code
src/
├── models/
│   └── todo.py          # Todo entity & validation
├── services/
│   ├── todo_service.py  # Business logic
│   └── repository.py    # In-memory storage
├── cli/
│   └── console_app.py   # CLI menu & interaction loop
└── lib/
    └── utils.py         # Helpers & input handling
🧪 Testing (Phase I)
Testing is performed via:

Manual CLI interaction

Validation of all CRUD flows

Edge-case input handling

Agent-based spec & plan review

Automated tests are intentionally deferred to later phases.

🎯 Phase I Success Criteria
✔ All 5 basic Todo features implemented
✔ Strict in-memory behavior (no files, no DB)
✔ Clean, modular Python code
✔ Stable and user-friendly CLI
✔ Architecture ready for future phases

🚫 Explicitly Out of Scope
Web or GUI interfaces

File or database persistence

Authentication or multi-user support

AI or chatbot features

Deployment, containers, or cloud infra

🤝 Contributing
Contributions are welcome within Phase I scope.

Guidelines
Follow clean architecture principles

Keep logic framework-agnostic

Maintain deterministic behavior

No persistence or external dependencies

Match existing code style (PEP-8)

Please open an issue before submitting large changes.

