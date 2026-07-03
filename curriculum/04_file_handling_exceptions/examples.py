import os
import json

def run_examples():
    print("=== Module 4: File Handling & Exceptions Examples ===")
    
    # 1. Safe config loading
    print("\n[Example 1: Safe config loading]")
    config_file = "app_config.json"
    
    # Create a dummy config first
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump({"theme": "dark", "version": 1.0}, f)
        
    try:
        print(f"Reading from {config_file}...")
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
            print("Successfully loaded config:", config)
    except FileNotFoundError:
        print("Config file missing! Loading default settings.")
    except json.JSONDecodeError:
        print("Config file is corrupted!")
    finally:
        # Cleanup
        if os.path.exists(config_file):
            os.remove(config_file)
            print("Cleaned up config file.")
            
    # 2. Input validation with exceptions
    print("\n[Example 2: Input validation]")
    def process_age(age_str):
        try:
            age = int(age_str)
            if age < 0:
                raise ValueError("Age cannot be negative.")
            if age > 150:
                raise ValueError("Age seems unrealistically high.")
            print(f"Valid age processed: {age}")
        except ValueError as e:
            print(f"Invalid input: {e}")
            
    process_age("25")
    process_age("not a number")
    process_age("-5")

if __name__ == "__main__":
    run_examples()
