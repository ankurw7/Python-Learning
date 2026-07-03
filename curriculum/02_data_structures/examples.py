"""
Module: 02_data_structures
Topic: Lists, Dictionaries, and Sets
Description: Examples of using Python's built-in data structures.
"""

def example_lists() -> list[str]:
    """
    Demonstrates list operations.
    """
    fruits: list[str] = ["apple", "banana", "cherry"]
    
    # Appending
    fruits.append("date")
    
    # Slicing
    # Returns the first 2 items
    first_two = fruits[:2] 
    print(f"First two fruits: {first_two}")
    
    return fruits


def example_dictionaries() -> dict[str, int]:
    """
    Demonstrates dictionary operations.
    """
    # Mapping names to ages
    ages: dict[str, int] = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35
    }
    
    # Accessing
    print(f"Alice's age: {ages['Alice']}")
    
    # Adding/Updating
    ages["David"] = 40
    
    return ages


def example_sets_and_tuples() -> tuple[set[int], tuple[int, int]]:
    """
    Demonstrates sets (unique items) and tuples (immutable).
    """
    # Set: Removes duplicates
    numbers: list[int] = [1, 2, 2, 3, 3, 3]
    unique_numbers: set[int] = set(numbers)
    print(f"Unique numbers: {unique_numbers}")
    
    # Tuple: Cannot be changed
    coordinates: tuple[int, int] = (10, 20)
    # coordinates[0] = 15  # This would raise an error
    
    return unique_numbers, coordinates


def example_list_comprehension(numbers: list[int]) -> list[int]:
    """
    Demonstrates list comprehensions for concise loop logic.
    
    Args:
        numbers (list[int]): Input list of numbers.
        
    Returns:
        list[int]: List of squares of the input numbers.
    """
    squares = [x * x for x in numbers]
    return squares


if __name__ == "__main__":
    print("--- Lists ---")
    print(example_lists())
    
    print("\n--- Dictionaries ---")
    print(example_dictionaries())
    
    print("\n--- Sets & Tuples ---")
    print(example_sets_and_tuples())
    
    print("\n--- List Comprehension ---")
    print(f"Squares of [1, 2, 3]: {example_list_comprehension([1, 2, 3])}")
