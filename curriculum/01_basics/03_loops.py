"""
Topic: Loops
"""

def run():
    limit = 10
    print(f"Finding even numbers up to {limit}:")
    
    evens = []
    for i in range(limit):
        if i % 2 == 0:
            evens.append(i)
            
    print(f"Result: {evens}")

if __name__ == "__main__":
    run()
