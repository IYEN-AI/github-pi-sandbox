"""A tiny calculator module used for github-pi sandbox testing."""


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    # Intentional bug: no zero-division guard. Reported via issue → gp:auto-fix.
    return a / b
