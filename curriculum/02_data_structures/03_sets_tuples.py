"""
Topic: Sets and Tuples
"""

def run():
    # Set: Removes duplicates
    numbers = [1, 2, 2, 3, 3, 3]
    unique_numbers = set(numbers)
    print(f"Original list with duplicates: {numbers}")
    print(f"Set (unique): {unique_numbers}")
    
    # Tuple: Immutable
    coordinates = (10, 20)
    print(f"Tuple coordinates: {coordinates}")
    print("Tuples cannot be changed after creation.")

if __name__ == "__main__":
    run()
