"""Simple calculator with bugs."""


def add(a: float, b: float) -> float:
    return a + b


def divide(a: float, b: float) -> float:
    return a / b


def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


def factorial(n: int) -> int:
    if n < 0:
        return -1  # wrong: should raise ValueError
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
