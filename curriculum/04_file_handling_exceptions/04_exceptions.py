# 04_exceptions.py
# Example code demonstrating basic exception handling

print("--- Catching ZeroDivisionError ---")
try:
    print("Attempting to divide 10 by 0...")
    result = 10 / 0
    print("This line will never execute.")
except ZeroDivisionError:
    print("Caught an error! You cannot divide by zero.")

print("\n--- Catching FileNotFoundError ---")
try:
    print("Attempting to open 'does_not_exist.txt'...")
    with open("does_not_exist.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Caught an error! The file was not found.")

print("\nProgram finished successfully without crashing.")
