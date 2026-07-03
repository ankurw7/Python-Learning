# 06_user_input.py
# Example: Taking user input

name = input("What is your name? ")
print(f"Nice to meet you, {name}!")

age_str = input("How old are you? ")
# Input always returns a string, so we might need to convert it
try:
    age = int(age_str)
    print(f"Next year you will be {age + 1} years old.")
except ValueError:
    print("That doesn't look like a valid number!")
