# Todo Operations Contract

## Overview
This document defines the contract for all todo operations in the console application. These operations represent the core functionality that will be implemented in the service layer.

## Operations

### 1. Create Todo
- **Input**: title (string, required), description (string, optional)
- **Output**: todo object with all attributes including generated ID
- **Success**: Returns created todo with status "pending"
- **Errors**:
  - Invalid input (empty title) → Error message
  - System error → Error message

### 2. List All Todos
- **Input**: None
- **Output**: Array of all todo objects
- **Success**: Returns array of all todos in creation order
- **Errors**: None expected

### 3. Get Todo by ID
- **Input**: id (integer, required)
- **Output**: todo object or null if not found
- **Success**: Returns requested todo object
- **Errors**:
  - Todo not found → Error message

### 4. Update Todo
- **Input**: id (integer, required), title (string, optional), description (string, optional)
- **Output**: updated todo object
- **Success**: Returns updated todo object
- **Errors**:
  - Todo not found → Error message
  - Invalid input → Error message

### 5. Update Todo Status
- **Input**: id (integer, required), status (string, required - "pending" or "completed")
- **Output**: updated todo object
- **Success**: Returns todo object with new status
- **Errors**:
  - Todo not found → Error message
  - Invalid status → Error message

### 6. Delete Todo
- **Input**: id (integer, required)
- **Output**: boolean indicating success
- **Success**: Returns true if deletion successful
- **Errors**:
  - Todo not found → Error message

## Data Format
All todo objects follow the structure:
```
{
  "id": integer,
  "title": string,
  "description": string,
  "status": "pending" | "completed",
  "created_at": ISO8601 datetime string
}
```

## Error Format
All errors follow the format:
```
{
  "error": "descriptive error message"
}
```

## Validation Rules
- Title must be non-empty for all operations
- ID must be valid and exist for update/delete operations
- Status must be either "pending" or "completed" for status updates