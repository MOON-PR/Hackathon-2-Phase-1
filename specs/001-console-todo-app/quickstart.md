# Quickstart Guide: Console Todo Application

## Prerequisites
- Python 3.13+
- UV package manager (optional, for dependency management)

## Setup
1. Clone or create the project directory
2. Ensure Python 3.13+ is installed and accessible
3. (Optional) Install dependencies using UV if any external packages are added

## Running the Application
1. Navigate to the project root directory
2. Execute the main application file:
   ```bash
   python src/cli/console_app.py
   ```
3. The application will start and display the main menu

## Basic Usage
1. **Add Todo**: Select option to add a new todo, enter title and optional description
2. **View Todos**: Select option to list all todos with their status indicators
3. **Update Todo**: Select option to modify an existing todo by ID
4. **Mark Complete/Incomplete**: Select option to change the status of a todo by ID
5. **Delete Todo**: Select option to remove a todo by ID
6. **Exit**: Select option to quit the application

## Expected Output
- Clear menu prompts with numbered options
- Formatted list of todos showing ID, title, status, and description
- Confirmation messages for all operations
- Error messages for invalid inputs or operations

## Example Workflow
1. Start the application
2. Add a few todo items
3. View the list to see all todos
4. Mark some as complete
5. Update details of an existing todo
6. Delete completed todos when finished
7. Exit the application

## Troubleshooting
- If the application fails to start, verify Python 3.13+ is installed
- If commands don't work, check that you're following the menu prompts exactly
- For invalid input errors, ensure you're providing required information as prompted