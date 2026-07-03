# 05_advanced_exceptions.py
# Example code demonstrating else, finally, and raise

print("--- Else and Finally blocks ---")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        # Runs ONLY if no exception occurred
        print(f"Success! {a} / {b} = {result}")
    finally:
        # Runs no matter what
        print("Cleanup: Operation attempted.")

print("Trying 10 / 2:")
divide(10, 2)
print("\nTrying 10 / 0:")
divide(10, 0)

print("\n--- Raising Exceptions ---")

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age set to {age}")

try:
    check_age(-5)
except ValueError as e:
    print(f"Caught a raised exception: {e}")
