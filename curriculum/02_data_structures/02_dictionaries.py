"""
Topic: Dictionaries
"""

def run():
    # Mapping names to ages
    ages = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35
    }
    print(f"Dictionary: {ages}")
    
    # Accessing
    print(f"Alice's age: {ages['Alice']}")
    
    # Adding/Updating
    ages["David"] = 40
    print(f"After adding David: {ages}")

if __name__ == "__main__":
    run()
