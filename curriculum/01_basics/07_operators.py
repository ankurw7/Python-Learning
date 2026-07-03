"""
Topic: Arithmetic and Logical Operators
"""

def run():
    # Arithmetic operators
    x = 10
    y = 3
    print(f"Addition: {x} + {y} = {x + y}")
    print(f"Subtraction: {x} - {y} = {x - y}")
    print(f"Multiplication: {x} * {y} = {x * y}")
    print(f"Division: {x} / {y} = {x / y}")
    print(f"Floor Division: {x} // {y} = {x // y}")
    print(f"Modulo: {x} % {y} = {x % y}")
    print(f"Exponentiation: {x} ** {y} = {x ** y}")

    # Logical operators
    has_pass = True
    is_adult = False
    print(f"\nLogical AND: {has_pass} and {is_adult} = {has_pass and is_adult}")
    print(f"Logical OR: {has_pass} or {is_adult} = {has_pass or is_adult}")
    print(f"Logical NOT: not {has_pass} = {not has_pass}")

if __name__ == "__main__":
    run()
