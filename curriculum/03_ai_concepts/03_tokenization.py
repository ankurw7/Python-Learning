"""
Topic: Tokenization
"""

def run():
    sentence = "Hello, AI World! This is Python."
    print(f"Original: {sentence}")
    
    # Simple punctuation removal
    clean_text = ""
    for char in sentence:
        if char.isalnum() or char.isspace():
            clean_text += char
            
    tokens = clean_text.lower().split()
    print(f"Tokens: {tokens}")

if __name__ == "__main__":
    run()
