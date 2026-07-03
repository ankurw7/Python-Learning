"""
Module: 01_basics
Topic: Variables and Control Flow
Description: Examples of basic Python syntax optimized for clarity and static analysis.
"""

def example_variables() -> None:
    """
    Demonstrates variable assignment and basic data types.
    """
    # Integer
    count: int = 10
    print(f"Count is an integer: {count}")

    # Float
    pi: float = 3.14159
    print(f"Pi is a float: {pi}")

    # String
    greeting: str = "Hello, AI!"
    print(f"Greeting is a string: {greeting}")

    # Boolean
    is_active: bool = True
    print(f"Is Active is a boolean: {is_active}")


def example_conditionals(value: int) -> str:
    """
    Demonstrates if-elif-else logic.
    
    Args:
        value (int): The number to check.
        
    Returns:
        str: A description of the number's magnitude.
    """
    if value < 0:
        return "Negative"
    elif value == 0:
        return "Zero"
    elif value < 10:
        return "Small Positive"
    else:
        return "Large Positive"


def example_loops(limit: int) -> list[int]:
    """
    Demonstrates a for loop.
    
    Args:
        limit (int): The upper bound (exclusive).
        
    Returns:
        list[int]: A list of even numbers up to the limit.
    """
    evens: list[int] = []
    for i in range(limit):
        if i % 2 == 0:
            evens.append(i)
    return evens


def example_operators(x: int, y: int) -> dict[str, float]:
    """
    Demonstrates arithmetic and logical operations.
    """
    return {
        "addition": float(x + y),
        "floor_division": float(x // y),
        "modulo": float(x % y),
        "exponent": float(x ** y),
        "logical_and": float(x > 0 and y > 0)
    }


def example_type_casting(val: any) -> str:
    """
    Demonstrates explicit type casting.
    """
    try:
        # Try converting to integer
        return f"Integer: {int(val)}"
    except (ValueError, TypeError):
        try:
            # Try converting to float
            return f"Float: {float(val)}"
        except (ValueError, TypeError):
            # Fallback to string
            return f"String: {str(val)}"


if __name__ == "__main__":
    print("--- Variables Example ---")
    example_variables()
    
    print("\n--- Conditionals Example ---")
    print(f"Check 5: {example_conditionals(5)}")
    print(f"Check 15: {example_conditionals(15)}")
    
    print("\n--- Loops Example ---")
    print(f"Evens up to 10: {example_loops(10)}")
    
    print("\n--- Operators Example ---")
    print(f"Operators with (10, 3): {example_operators(10, 3)}")
    
    print("\n--- Type Casting Example ---")
    print(f"Cast '123': {example_type_casting('123')}")
    print(f"Cast '3.14': {example_type_casting('3.14')}")
    print(f"Cast 'hello': {example_type_casting('hello')}")
