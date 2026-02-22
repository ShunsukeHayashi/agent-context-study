# Task Manager - Project Overview

## Architecture
Python CLI task manager with two core modules:

- `src/task_manager.py` - CRUD operations for tasks
- `src/formatter.py` - Display formatting and statistics

## Data Model
Tasks stored in `data/tasks.json` as flat JSON array.
Fields: id, title, priority (high/medium/low), status (pending/done), created_at, completed_at

## Known Issues
1. `delete_task()` always returns True regardless of whether the task existed - callers cannot distinguish successful deletion from no-op
2. `format_summary()` crashes with ZeroDivisionError when called with an empty task list

## Testing
Tests in `tests/`. Use pytest.
