"""
Module: 01_basics
Topic: Exercises
Description: Practice problems for variables and control flow.
"""

def exercise_check_parity(number: int) -> str:
    """
    TODO: Implement this function.
    
    Return "Even" if the number is even, and "Odd" if it is odd.
    
    Args:
        number (int): The number to check.
        
    Returns:
        str: "Even" or "Odd".
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def exercise_sum_numbers(n: int) -> int:
    """
    TODO: Implement this function.
    
    Calculate the sum of all integers from 1 to n (inclusive).
    
    Args:
        n (int): The upper limit.
        
    Returns:
        int: The sum of 1..n.
    """
    return sum(range(1, n + 1))


def exercise_validate_password(password: str) -> bool:
    """
    TODO: Implement this function.
    
    Check if a password meets the following criteria:
    - At least 8 characters long.
    - Contains the word "AI".
    
    Args:
        password (str): The password to check.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    return len(password) >= 8 and "AI" in password


def exercise_celsius_to_fahrenheit(celsius: float) -> float:
    """
    TODO: Implement this function.
    
    Convert a temperature from Celsius to Fahrenheit using arithmetic operators.
    Formula: (Celsius * 9/5) + 32
    
    Args:
        celsius (float): The temperature in Celsius.
        
    Returns:
        float: The temperature in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def exercise_convert_and_sum(num1_str: str, num2_str: str) -> int:
    """
    TODO: Implement this function.
    
    Convert two string representations of numbers to integers and return their sum.
    
    Args:
        num1_str (str): The first number as a string.
        num2_str (str): The second number as a string.
        
    Returns:
        int: The sum of the two converted integers.
    """
    return int(num1_str) + int(num2_str)
