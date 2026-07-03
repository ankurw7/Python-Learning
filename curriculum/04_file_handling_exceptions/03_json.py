# 03_json.py
# Example code demonstrating JSON serialization
import json
import os

data = {
    "name": "Python Learner",
    "level": "Intermediate",
    "skills": ["Python", "File I/O", "JSON"],
    "active": True
}

print("--- Dictionary data ---")
print(data)
print(type(data))

print("\n--- Saving to JSON file ---")
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
print("Saved data to data.json")

print("\n--- Loading from JSON file ---")
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print("Loaded data:")
    print(loaded)
    print("Type after loading:", type(loaded))

# Cleanup
os.remove("data.json")
