# 06_string_methods.py
# Common string operations in Python

text = "  Hello, Python World!  "

print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Lower: '{text.lower()}'")
print(f"Upper: '{text.upper()}'")
print(f"Replace: '{text.replace('Python', 'AI')}'")

# Splitting and Joining
words = "apple,banana,cherry".split(",")
print(f"\nSplit by comma: {words}")

joined = " - ".join(words)
print(f"Joined with ' - ': {joined}")

# Checking content
print(f"\n'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'Hello'.startswith('He'): {'Hello'.startswith('He')}")
