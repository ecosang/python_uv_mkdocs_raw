"""
Arithmetic calculation functions for the demo program package.

This module provides a comprehensive set of mathematical functions for basic arithmetic
operations, advanced calculations, and utility functions. All functions include proper
type hints and comprehensive documentation for use with MkDocs.

Functions:
    add: Add two numbers
    subtract: Subtract two numbers
    multiply: Multiply two numbers
    divide: Divide two numbers
    power: Raise a number to a power
    square_root: Calculate square root
    factorial: Calculate factorial
    gcd: Calculate greatest common divisor
    lcm: Calculate least common multiple
    average: Calculate average of a list
    percentage: Calculate percentage
    round_to_decimal: Round to specified decimal places
"""

import math
from typing import Union, List


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together.
    
    Args:
        a: First number to add
        b: Second number to add
        
    Returns:
        Sum of a and b
        
    Example:
        >>> add(5, 3)
        8
        >>> add(2.5, 1.5)
        4.0
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract the second number from the first number.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
        
    Returns:
        Difference of a and b
        
    Example:
        >>> subtract(10, 4)
        6
        >>> subtract(5.5, 2.3)
        3.2
    """
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers together.
    
    Args:
        a: First number to multiply
        b: Second number to multiply
        
    Returns:
        Product of a and b
        
    Example:
        >>> multiply(6, 7)
        42
        >>> multiply(2.5, 3.0)
        7.5
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Divide the first number by the second number.
    
    Args:
        a: Numerator (number to be divided)
        b: Denominator (number to divide by)
        
    Returns:
        Quotient of a divided by b
        
    Raises:
        ZeroDivisionError: If b is zero
        
    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 3)
        2.3333333333333335
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    Raise a number to a specified power.
    
    Args:
        base: The base number
        exponent: The exponent to raise the base to
        
    Returns:
        base raised to the power of exponent
        
    Example:
        >>> power(2, 3)
        8
        >>> power(2.5, 2)
        6.25
    """
    return base ** exponent


def square_root(number: Union[int, float]) -> float:
    """
    Calculate the square root of a number.
    
    Args:
        number: Number to find square root of
        
    Returns:
        Square root of the number
        
    Raises:
        ValueError: If number is negative
        
    Example:
        >>> square_root(16)
        4.0
        >>> square_root(2)
        1.4142135623730951
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    The factorial of a number n is the product of all positive integers
    less than or equal to n. For example, 5! = 5 × 4 × 3 × 2 × 1 = 120.
    
    Args:
        n: Non-negative integer to calculate factorial for
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
        
    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two integers.
    
    The greatest common divisor (GCD) of two integers is the largest positive
    integer that divides both numbers without a remainder.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        Greatest common divisor of a and b
        
    Example:
        >>> gcd(48, 18)
        6
        >>> gcd(12, 8)
        4
    """
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """
    Calculate the least common multiple of two integers.
    
    The least common multiple (LCM) of two integers is the smallest positive
    integer that is divisible by both numbers.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        Least common multiple of a and b
        
    Example:
        >>> lcm(12, 18)
        36
        >>> lcm(8, 12)
        24
    """
    return abs(a * b) // math.gcd(a, b)


def average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the average (arithmetic mean) of a list of numbers.
    
    Args:
        numbers: List of numbers to calculate average for
        
    Returns:
        Average of the numbers
        
    Raises:
        ValueError: If the list is empty
        
    Example:
        >>> average([1, 2, 3, 4, 5])
        3.0
        >>> average([10.5, 20.5, 30.5])
        20.5
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def percentage(part: Union[int, float], total: Union[int, float]) -> float:
    """
    Calculate what percentage part is of total.
    
    This function returns the result as a decimal. To get the percentage,
    multiply the result by 100.
    
    Args:
        part: Part value
        total: Total value
        
    Returns:
        Percentage as a decimal (multiply by 100 for percentage)
        
    Raises:
        ZeroDivisionError: If total is zero
        
    Example:
        >>> percentage(25, 100)
        0.25
        >>> percentage(3, 10)
        0.3
        >>> percentage(25, 100) * 100  # To get actual percentage
        25.0
    """
    if total == 0:
        raise ZeroDivisionError("Total cannot be zero")
    return part / total


def round_to_decimal(number: float, decimal_places: int = 2) -> float:
    """
    Round a number to a specified number of decimal places.
    
    Args:
        number: Number to round
        decimal_places: Number of decimal places to round to (default: 2)
        
    Returns:
        Rounded number
        
    Example:
        >>> round_to_decimal(3.14159)
        3.14
        >>> round_to_decimal(3.14159, 4)
        3.1416
        >>> round_to_decimal(2.5, 0)
        2.0
    """
    return round(number, decimal_places) 