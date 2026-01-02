from typing import Optional
from src.services.todo_service import TodoService
from src.services.repository import TodoRepository
from src.models.todo import Todo
from src.lib.utils import format_error, TodoNotFoundError, ValidationError

class ConsoleApp:
    """
    Console application for the Todo app.
    Provides the main menu and user interaction interface.
    """
    def __init__(self):
        self.repository = TodoRepository()
        self.service = TodoService(self.repository)
        self.running = True

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*50)
        print("TODO APPLICATION")
        print("="*50)
        print("1. Add Todo")
        print("2. List Todos")
        print("3. Update Todo")
        print("4. Mark Todo Complete/Incomplete")
        print("5. Delete Todo")
        print("6. Exit")
        print("-"*50)

    def get_user_choice(self) -> str:
        """Get the user's menu choice."""
        try:
            choice = input("Enter your choice (1-6): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            return "6"  # Treat as exit

    def add_todo(self):
        """Handle adding a new todo."""
        print("\n--- Add New Todo ---")
        title = input("Enter title: ").strip()

        if not title:
            print(format_error("Title cannot be empty")["error"])
            return

        description = input("Enter description (optional, press Enter to skip): ").strip()
        if not description:
            description = None

        try:
            todo = self.service.add_todo(title, description)
            print(f"✓ Todo added successfully with ID: {todo.id}")
        except ValidationError as e:
            print(format_error(str(e))["error"])

    def list_todos(self):
        """Handle listing all todos."""
        print("\n--- All Todos ---")
        todos = self.service.list_todos()

        if not todos:
            print("No todos found.")
            return

        for todo in todos:
            status_indicator = "X" if todo.status == "completed" else "O"
            print(f"[{status_indicator}] ID: {todo.id} | Title: {todo.title}")
            if todo.description:
                print(f"    Description: {todo.description}")
            print(f"    Created: {todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 40)

    def update_todo(self):
        """Handle updating a todo."""
        print("\n--- Update Todo ---")
        try:
            todo_id = int(input("Enter todo ID to update: ").strip())
        except ValueError:
            print(format_error("Invalid ID format")["error"])
            return

        # Get the current todo to show current values
        try:
            current_todo = self.service.get_todo(todo_id)
            print(f"Current title: {current_todo.title}")
            if current_todo.description:
                print(f"Current description: {current_todo.description}")
        except TodoNotFoundError:
            print(format_error(f"Todo with ID {todo_id} not found")["error"])
            return

        new_title = input("Enter new title (press Enter to keep current): ").strip()
        if not new_title:
            new_title = None

        new_description = input("Enter new description (press Enter to keep current): ").strip()
        if not new_description:
            new_description = None

        try:
            updated_todo = self.service.update_todo(todo_id, new_title, new_description)
            print(f"✓ Todo {updated_todo.id} updated successfully")
        except ValidationError as e:
            print(format_error(str(e))["error"])
        except TodoNotFoundError as e:
            print(format_error(str(e))["error"])

    def update_todo_status(self):
        """Handle updating a todo's status."""
        print("\n--- Update Todo Status ---")
        try:
            todo_id = int(input("Enter todo ID: ").strip())
        except ValueError:
            print(format_error("Invalid ID format")["error"])
            return

        try:
            current_todo = self.service.get_todo(todo_id)
            print(f"Current status for '{current_todo.title}': {current_todo.status}")
        except TodoNotFoundError:
            print(format_error(f"Todo with ID {todo_id} not found")["error"])
            return

        print("Select new status:")
        print("1. Pending")
        print("2. Completed")
        status_choice = input("Enter choice (1-2): ").strip()

        if status_choice == "1":
            new_status = "pending"
        elif status_choice == "2":
            new_status = "completed"
        else:
            print(format_error("Invalid choice. Please enter 1 or 2.")["error"])
            return

        try:
            updated_todo = self.service.update_status(todo_id, new_status)
            print(f"✓ Todo {updated_todo.id} status updated to {new_status}")
        except ValidationError as e:
            print(format_error(str(e))["error"])
        except TodoNotFoundError as e:
            print(format_error(str(e))["error"])

    def delete_todo(self):
        """Handle deleting a todo."""
        print("\n--- Delete Todo ---")
        try:
            todo_id = int(input("Enter todo ID to delete: ").strip())
        except ValueError:
            print(format_error("Invalid ID format")["error"])
            return

        try:
            self.service.delete_todo(todo_id)
            print(f"✓ Todo with ID {todo_id} deleted successfully")
        except TodoNotFoundError as e:
            print(format_error(str(e))["error"])

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo Application!")
        print("This is an in-memory console application.")

        while self.running:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_todo()
            elif choice == "2":
                self.list_todos()
            elif choice == "3":
                self.update_todo()
            elif choice == "4":
                self.update_todo_status()
            elif choice == "5":
                self.delete_todo()
            elif choice == "6":
                print("Thank you for using the Todo Application. Goodbye!")
                self.running = False
            else:
                print("Invalid choice. Please enter a number between 1-6.")

def main():
    """Main entry point for the application."""
    app = ConsoleApp()
    app.run()

if __name__ == "__main__":
    main()