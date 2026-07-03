"""
Topic: Type Casting (Conversion)
"""

def run():
    # Explicit Type Casting
    num_str = "123"
    num_int = int(num_str)
    print(f"String to Integer: '{num_str}' -> {num_int} (Type: {type(num_int)})")

    float_str = "3.14"
    float_val = float(float_str)
    print(f"String to Float: '{float_str}' -> {float_val} (Type: {type(float_val)})")

    int_val = 42
    str_val = str(int_val)
    print(f"Integer to String: {int_val} -> '{str_val}' (Type: {type(str_val)})")

    # Truthy and Falsy values
    print(f"\nTruthiness of 'hello': {bool('hello')}")
    print(f"Truthiness of '': {bool('')}")
    print(f"Truthiness of 0: {bool(0)}")
    print(f"Truthiness of 42: {bool(42)}")

if __name__ == "__main__":
    run()
