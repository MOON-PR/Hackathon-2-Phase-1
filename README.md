# Console Todo Application

An in-memory Python console-based todo application that demonstrates a full agentic development workflow.

## Features

- Add, list, update, delete, and mark todos as complete/incomplete
- All data stored in memory (no persistence)
- Console-based user interface
- Clear status indicators for todos
- Input validation and error handling

## Requirements

- Python 3.13+

## Installation

1. Clone or download the repository
2. Ensure Python 3.13+ is installed

## Usage

Run the application:

```bash
python src/cli/console_app.py
```

Follow the on-screen menu prompts to:
1. Add new todos
2. List all todos
3. Update todo details
4. Mark todos as complete/incomplete
5. Delete todos

## Architecture

The application follows a layered architecture:

- **Models**: Data structures (Todo model)
- **Services**: Business logic (TodoService)
- **Repository**: Data access (TodoRepository)
- **CLI**: User interface (ConsoleApp)

## Project Structure

```
src/
├── models/
│   └── todo.py          # Todo data structure and validation
├── services/
│   ├── todo_service.py  # Business logic for todo operations
│   └── repository.py    # In-memory storage operations
├── cli/
│   └── console_app.py   # Main console application and menu system
└── lib/
    └── utils.py         # Utility functions and error handling
```

## Testing

The application can be tested by running it and performing all supported operations through the console interface.