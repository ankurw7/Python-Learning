# 01_reading.py
# Example code demonstrating file reading
import os

# Create a sample file to read
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Line 1: Hello World!\nLine 2: Python is fun.\nLine 3: File handling is easy.")

print("--- Reading entire file ---")
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

print("\n--- Iterating line by line ---")
with open("sample.txt", "r", encoding="utf-8") as file:
    for i, line in enumerate(file, 1):
        print(f"Line {i}: {line.strip()}")

# Cleanup
os.remove("sample.txt")
