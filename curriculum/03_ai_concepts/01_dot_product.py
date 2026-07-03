"""
Topic: Dot Product
"""

def run():
    vector_a = [1.0, 2.0, 3.0]
    vector_b = [0.5, 0.5, 0.5]
    
    print(f"Vector A: {vector_a}")
    print(f"Vector B: {vector_b}")
    
    # Calculate dot product
    # zip pairs elements: (a[0], b[0]), (a[1], b[1])...
    products = [a * b for a, b in zip(vector_a, vector_b)]
    dot_product = sum(products)
    
    print(f"Dot Product: {dot_product}")

if __name__ == "__main__":
    run()
