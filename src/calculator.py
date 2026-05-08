"""A tiny calculator module used for github-pi sandbox testing."""


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: int, exponent: int) -> float:
    """Raise base to the given exponent."""
    result = 1
    for _ in range(exponent):
        result *= base
    return float(result)
