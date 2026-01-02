from typing import List, Optional
from src.models.todo import Todo
from src.services.repository import TodoRepository
from src.lib.utils import validate_todo_data, ValidationError, TodoNotFoundError
from datetime import datetime

class TodoService:
    """
    Service layer for todo operations.
    Handles business logic and validation for todo operations.
    """
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def add_todo(self, title: str, description: Optional[str] = None) -> Todo:
        """
        Add a new todo with the given title and optional description.
        The todo will have 'pending' status by default.
        """
        # Validate the input data
        validate_todo_data(title=title, description=description)

        # Create a new todo with auto-generated ID and pending status
        todo = Todo(
            id=0,  # Will be assigned by repository
            title=title,
            description=description,
            status="pending",
            created_at=datetime.now()
        )

        # Save to repository (which will assign the ID)
        return self.repository.create(todo)

    def list_todos(self) -> List[Todo]:
        """
        List all todos.
        """
        return self.repository.list_all()

    def get_todo(self, todo_id: int) -> Todo:
        """
        Get a specific todo by ID.
        """
        return self.repository.get_by_id(todo_id)

    def update_todo(self, todo_id: int, title: Optional[str] = None,
                    description: Optional[str] = None) -> Todo:
        """
        Update a todo's title and/or description.
        """
        # Validate the input data if provided
        validate_todo_data(title=title, description=description)

        # Update the todo in the repository
        return self.repository.update(todo_id, title, description)

    def update_status(self, todo_id: int, status: str) -> Todo:
        """
        Update a todo's status to either 'pending' or 'completed'.
        """
        # Validate the status
        validate_todo_data(status=status)

        # Update the status in the repository
        return self.repository.update_status(todo_id, status)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by ID.
        """
        return self.repository.delete(todo_id)