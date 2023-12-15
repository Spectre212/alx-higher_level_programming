#!/usr/bin/python3

def add(a, b):
    """Addition function.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The result of a + b.
    """
    return a + b


def sub(a, b):
    """Subtraction function.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The result of a - b.
    """
    return a - b


def mul(a, b):
    """Multiplication function.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The result of a * b.
    """
    return a * b


def div(a, b):
    """Division function.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The result of a / b.
    """
    if b != 0:
        return int(a / b)
    else:
        raise ValueError("Division by zero is undefined.")
