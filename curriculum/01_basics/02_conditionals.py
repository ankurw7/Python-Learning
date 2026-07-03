"""
Topic: Conditionals
"""

def run():
    value = 5
    print(f"Checking value: {value}")
    
    if value < 0:
        print("Result: Negative")
    elif value == 0:
        print("Result: Zero")
    elif value < 10:
        print("Result: Small Positive")
    else:
        print("Result: Large Positive")

if __name__ == "__main__":
    run()
