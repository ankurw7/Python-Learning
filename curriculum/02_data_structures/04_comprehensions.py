"""
Topic: List Comprehensions
"""

def run():
    numbers = [1, 2, 3, 4, 5]
    print(f"Original numbers: {numbers}")
    
    # Create a new list of squares
    squares = [x * x for x in numbers]
    print(f"Squares (using comprehension): {squares}")

if __name__ == "__main__":
    run()
