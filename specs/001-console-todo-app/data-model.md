# Data Model: Console Todo Application

## Todo Entity

### Attributes
- **id**: Integer (required, unique, auto-generated)
  - Primary identifier for the todo item
  - Auto-incremented for each new todo
  - Used for all CRUD operations

- **title**: String (required, non-empty)
  - Human-readable name/description of the task
  - Must be non-empty to ensure meaningful todos
  - Max length: 200 characters

- **description**: String (optional)
  - Additional details about the todo task
  - Can be empty or null
  - Max length: 1000 characters

- **status**: String (required, default: "pending")
  - Current state of the todo item
  - Valid values: "pending", "completed"
  - Default value: "pending" when created

- **created_at**: DateTime (required, auto-generated)
  - Timestamp when the todo was created
  - Used for ordering and tracking purposes
  - Format: ISO 8601 string

### Validation Rules
1. **Title Required**: All todos must have a non-empty title
2. **Status Validation**: Status must be either "pending" or "completed"
3. **ID Uniqueness**: Each todo must have a unique ID
4. **Length Limits**: Title ≤ 200 chars, Description ≤ 1000 chars

### State Transitions
- **pending → completed**: When user marks todo as complete
- **completed → pending**: When user marks todo as incomplete

### Relationships
- None (standalone entity)

## Todo Collection

### Structure
- **Storage Type**: Dictionary mapping ID to Todo objects
- **Key**: Integer ID
- **Value**: Todo object instance
- **Access Pattern**: O(1) lookup by ID

### Operations
- **Create**: Add new todo with auto-generated ID
- **Read**: Retrieve todo by ID or list all todos
- **Update**: Modify existing todo properties
- **Delete**: Remove todo by ID
- **Find**: Search/filter todos by status or other criteria