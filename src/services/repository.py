from typing import Dict, List, Optional
from src.models.todo import Todo
from src.lib.utils import TodoNotFoundError
from datetime import datetime

class TodoRepository:
    """
    Repository for managing todos in memory.
    Provides CRUD operations for todo items.
    """
    def __init__(self):
        self._todos: Dict[int, Todo] = {}
        self._next_id = 1

    def create(self, todo: Todo) -> Todo:
        """
        Create a new todo with an auto-generated ID.
        """
        # Assign the next available ID to the todo
        todo.id = self._next_id
        self._todos[todo.id] = todo
        self._next_id += 1
        return todo

    def get_by_id(self, todo_id: int) -> Todo:
        """
        Retrieve a todo by its ID.
        Raises TodoNotFoundError if not found.
        """
        if todo_id not in self._todos:
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")
        return self._todos[todo_id]

    def list_all(self) -> List[Todo]:
        """
        Retrieve all todos.
        """
        return list(self._todos.values())

    def update(self, todo_id: int, title: Optional[str] = None,
               description: Optional[str] = None) -> Todo:
        """
        Update an existing todo's title and/or description.
        Raises TodoNotFoundError if not found.
        """
        if todo_id not in self._todos:
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")

        todo = self._todos[todo_id]

        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description

        return todo

    def update_status(self, todo_id: int, status: str) -> Todo:
        """
        Update the status of a todo.
        Raises TodoNotFoundError if not found.
        """
        if todo_id not in self._todos:
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")

        if status not in ["pending", "completed"]:
            raise ValueError(f"Status must be 'pending' or 'completed', got '{status}'")

        todo = self._todos[todo_id]
        todo.status = status
        return todo

    def delete(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.
        Returns True if deletion was successful, False if todo didn't exist.
        """
        if todo_id not in self._todos:
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")

        del self._todos[todo_id]
        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID (for testing purposes).
        """
        return self._next_id