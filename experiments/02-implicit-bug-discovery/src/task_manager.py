"""Task Manager - Simple CLI task management tool."""

import json
from datetime import datetime
from pathlib import Path

TASKS_FILE = Path(__file__).parent.parent / "data" / "tasks.json"


def load_tasks() -> list[dict]:
    """Load tasks from JSON file."""
    if not TASKS_FILE.exists():
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks: list[dict]) -> None:
    """Save tasks to JSON file."""
    TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(title: str, priority: str = "medium") -> dict:
    """Add a new task."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)
    return task


def list_tasks(status: str = None) -> list[dict]:
    """List tasks, optionally filtered by status."""
    tasks = load_tasks()
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    return tasks


def complete_task(task_id: int) -> dict | None:
    """Mark a task as complete."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["completed_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            return task
    return None


def delete_task(task_id: int) -> bool:
    """Delete a task by ID."""
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(new_tasks)
    return True
