# 05_functions.py
# Example: Defining and calling functions

def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Using the functions
greet("Learner")

result = add_numbers(5, 7)
print(f"5 + 7 = {result}")

# Function with default argument
def power(base, exponent=2):
    return base ** exponent

print(f"3 squared is {power(3)}")
print(f"3 cubed is {power(3, 3)}")
