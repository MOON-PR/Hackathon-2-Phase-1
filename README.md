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
```

---

## 🚀 Features (Phase I)

✔ Add todos (title + description)  
✔ List todos with status indicators  
✔ Update todo details  
✔ Mark todos as complete / incomplete  
✔ Delete todos by ID  

> ⚠️ All data is stored **only in memory**.  
> Restarting the app clears all todos — by design.

---

## 🎞️ CLI Demo (GIF-Style)

```text
▶ python src/cli/console_app.py

📝 Todo Application
──────────────────
1. Add Todo
2. List Todos
3. Update Todo
4. Mark Complete / Incomplete
5. Delete Todo
6. Exit
```

```text
▶ Add Todo
Title: Buy groceries
Description: Milk, eggs, bread

✅ Todo added successfully!
```

```text
▶ List Todos

[1] Buy groceries
    Status: ⏳ Pending
    Description: Milk, eggs, bread
```

```text
▶ Mark Complete

✔ Todo marked as completed!
```

```text
▶ List Todos

[1] Buy groceries
    Status: ✅ Completed
```

---

## 🧩 Tech Stack

| Category | Choice |
|--------|-------|
| Language | Python **3.13+** |
| Interface | Console / CLI |
| Storage | In-memory (Python data structures) |
| Tooling | Agentic Dev Stack, Claude Code |
| Style | Clean Architecture, PEP-8 |

---

## ⚙️ Installation

```bash
git clone <repo-url>
cd console-todo-app
python --version
```

---

## ▶️ Usage

```bash
python src/cli/console_app.py
```

---

## 🏗️ Architecture

```text
User Input
   ↓
Console UI (CLI)
   ↓
TodoService (Business Logic)
   ↓
TodoRepository (In-Memory Store)
   ↓
Todo Model
```

---

## 📁 Project Structure

```text
src/
├── models/
│   └── todo.py
├── services/
│   ├── todo_service.py
│   └── repository.py
├── cli/
│   └── console_app.py
└── lib/
    └── utils.py
```

---

## 🤝 Contributing

- Keep changes within Phase I scope
- Follow clean architecture principles
- No persistence or external dependencies
- Match PEP-8 style

---

## 📜 License

MIT — free to use, modify, and extend.

Phase I complete.
Simple by design. Solid by intention.
