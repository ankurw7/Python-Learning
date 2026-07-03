"""
Topic: Lists
"""

def run():
    fruits = ["apple", "banana", "cherry"]
    print(f"Original list: {fruits}")
    
    # Appending
    fruits.append("date")
    print(f"After appending 'date': {fruits}")
    
    # Slicing
    first_two = fruits[:2] 
    print(f"First two items: {first_two}")

if __name__ == "__main__":
    run()
