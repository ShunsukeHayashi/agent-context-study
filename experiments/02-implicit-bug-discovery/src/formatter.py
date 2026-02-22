"""Output formatter for task display."""


def format_task(task: dict) -> str:
    """Format a single task for display."""
    status_icon = "✅" if task["status"] == "done" else "⏳"
    priority_colors = {"high": "🔴", "medium": "🟡", "low": "🟢"}
    icon = priority_colors.get(task["priority"], "⚪")
    return f"{status_icon} [{task['id']}] {icon} {task['title']}"


def format_task_list(tasks: list[dict]) -> str:
    """Format a list of tasks."""
    if not tasks:
        return "No tasks found."
    return "\n".join(format_task(t) for t in tasks)


def format_summary(tasks: list[dict]) -> dict:
    """Generate summary statistics."""
    total = len(tasks)
    done = sum(1 for t in tasks if t["status"] == "done")
    pending = total - done
    completion_rate = done / total * 100
    return {
        "total": total,
        "done": done,
        "pending": pending,
        "completion_rate": f"{completion_rate:.1f}%",
    }
