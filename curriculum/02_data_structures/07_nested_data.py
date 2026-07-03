# 07_nested_data.py
# Working with nested lists and dictionaries

# Nested List (2D matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print(f"\nElement at [1][2]: {matrix[1][2]}")  # Row 1, Column 2 -> 6

# Nested Dictionary
users = {
    "alice": {"age": 30, "city": "NYC"},
    "bob": {"age": 25, "city": "LA"}
}

print(f"\nAlice's city: {users['alice']['city']}")

# Iterating nested dict
print("\nAll users:")
for name, info in users.items():
    print(f"  {name}: {info['age']} years old, lives in {info['city']}")
