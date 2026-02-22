"""Simple calculator module."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    return a / b  # BUG: no zero division guard


def average(numbers: list[float]) -> float:
    """Calculate average of a list of numbers."""
    return sum(numbers) / len(numbers)  # BUG: empty list crashes


def percentage(value: float, total: float) -> float:
    """Calculate what percentage value is of total."""
    return (value / total) * 100  # BUG: no zero guard
