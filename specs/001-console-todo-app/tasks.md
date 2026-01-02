---
description: "Task list for Console Todo Application"
---

# Tasks: Console Todo Application

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 [P] Create source directory structure: src/models/, src/services/, src/cli/, src/lib/
- [X] T003 [P] Create test directory structure: tests/unit/, tests/integration/, tests/contract/
- [X] T004 Initialize Python project with basic configuration

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Create Todo data model in src/models/todo.py
- [X] T006 Create TodoRepository for in-memory operations in src/services/repository.py
- [X] T007 [P] Create utility functions in src/lib/utils.py
- [X] T008 Create TodoService with basic operations in src/services/todo_service.py
- [X] T009 Implement error handling structures in src/lib/utils.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items with title and optional description, assigning unique IDs and storing in memory with pending status

**Independent Test**: Running the application and adding a todo item, verifying it appears in the list with a unique ID and pending status

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

- [X] T010 [P] [US1] Unit test for Todo creation in tests/unit/models/test_todo.py
- [X] T011 [P] [US1] Unit test for TodoService.create_todo in tests/unit/services/test_todo_service.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement Todo model with validation in src/models/todo.py
- [X] T013 [US1] Implement TodoRepository.create method in src/services/repository.py
- [X] T014 [US1] Implement TodoService.add_todo method in src/services/todo_service.py
- [X] T015 [US1] Implement console input for adding todo in src/cli/console_app.py
- [X] T016 [US1] Add validation for non-empty title in src/models/todo.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View/List Todos (Priority: P1)

**Goal**: Enable users to view all their todo items with clear status indicators showing IDs, titles, descriptions, and completion status

**Independent Test**: Adding some todos and then viewing the list to confirm all items appear with correct status indicators

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T017 [P] [US2] Unit test for TodoService.list_todos in tests/unit/services/test_todo_service.py
- [X] T018 [P] [US2] Unit test for TodoService.get_todo in tests/unit/services/test_todo_service.py

### Implementation for User Story 2

- [X] T019 [P] [US2] Implement TodoRepository.list_all method in src/services/repository.py
- [X] T020 [P] [US2] Implement TodoRepository.get_by_id method in src/services/repository.py
- [X] T021 [US2] Implement TodoService.list_todos method in src/services/todo_service.py
- [X] T022 [US2] Implement console display for listing todos in src/cli/console_app.py
- [X] T023 [US2] Add clear status indicators in console output

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Update Todo Details (Priority: P2)

**Goal**: Enable users to modify the details of existing todo items by their ID (title or description)

**Independent Test**: Creating a todo, updating its details, and verifying the changes are reflected when viewing the list

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T024 [P] [US3] Unit test for TodoService.update_todo in tests/unit/services/test_todo_service.py

### Implementation for User Story 3

- [X] T025 [P] [US3] Implement TodoRepository.update method in src/services/repository.py
- [X] T026 [US3] Implement TodoService.update_todo method in src/services/todo_service.py
- [X] T027 [US3] Implement console input for updating todo in src/cli/console_app.py
- [X] T028 [US3] Add validation for update operations in src/models/todo.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---
## Phase 6: User Story 4 - Mark Todo Complete/Incomplete (Priority: P2)

**Goal**: Enable users to update the status of specific todo items by their ID (complete or incomplete)

**Independent Test**: Creating a todo, marking it complete, verifying the status change, and then marking it incomplete again

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T029 [P] [US4] Unit test for TodoService.update_status in tests/unit/services/test_todo_service.py

### Implementation for User Story 4

- [X] T030 [P] [US4] Implement TodoRepository.update_status method in src/services/repository.py
- [X] T031 [US4] Implement TodoService.update_status method in src/services/todo_service.py
- [X] T032 [US4] Implement console input for updating todo status in src/cli/console_app.py
- [X] T033 [US4] Add validation for status updates in src/models/todo.py

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---
## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Enable users to remove specific todo items by their ID

**Independent Test**: Creating a todo, deleting it, and verifying it no longer appears in the list

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T034 [P] [US5] Unit test for TodoService.delete_todo in tests/unit/services/test_todo_service.py

### Implementation for User Story 5

- [X] T035 [P] [US5] Implement TodoRepository.delete method in src/services/repository.py
- [X] T036 [US5] Implement TodoService.delete_todo method in src/services/todo_service.py
- [X] T037 [US5] Implement console input for deleting todo in src/cli/console_app.py
- [X] T038 [US5] Add error handling for non-existent todos in src/services/todo_service.py

**Checkpoint**: All user stories should now be independently functional

---
## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T039 [P] Add comprehensive error handling throughout the application
- [X] T040 [P] Implement edge case handling (non-existent todos, invalid input)
- [X] T041 [P] Add input validation across all operations
- [X] T042 [P] Create main application entry point in src/cli/console_app.py
- [X] T043 [P] Add application startup and menu system in src/cli/console_app.py
- [X] T044 [P] Add application documentation and usage instructions
- [X] T045 Run quickstart.md validation to ensure application works as expected

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence