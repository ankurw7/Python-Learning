# 02_writing.py
# Example code demonstrating file writing
import os

print("--- Writing to a file ('w' mode) ---")
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("This is a fresh new file.\n")
    f.write("This mode overwrites any existing content.\n")
print("Data written successfully.")

print("\n--- Appending to a file ('a' mode) ---")
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("This line was appended to the end!\n")
print("Data appended successfully.")

print("\n--- Verifying Content ---")
with open("output.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Cleanup
os.remove("output.txt")
