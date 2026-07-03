"""
Module: 03_ai_concepts
Topic: Math and Logic for AI
Description: Implementing core AI concepts using pure Python to understand the underlying mechanics.
"""

import math

def example_dot_product(vector_a: list[float], vector_b: list[float]) -> float:
    """
    Calculates the dot product of two vectors.
    Dot product is fundamental in neural networks (inputs * weights).
    
    Args:
        vector_a (list[float]): First vector.
        vector_b (list[float]): Second vector.
        
    Returns:
        float: The sum of the products of corresponding entries.
    """
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be of same length")
        
    # zip pairs elements: (a[0], b[0]), (a[1], b[1])...
    products = [a * b for a, b in zip(vector_a, vector_b)]
    return sum(products)


def example_mean_squared_error(predictions: list[float], targets: list[float]) -> float:
    """
    Calculates Mean Squared Error (MSE), a common loss function.
    
    Args:
        predictions (list[float]): Model outputs.
        targets (list[float]): Actual values.
        
    Returns:
        float: The average squared difference.
    """
    if len(predictions) != len(targets):
        raise ValueError("Lists must be of same length")
        
    squared_errors = [(p - t) ** 2 for p, t in zip(predictions, targets)]
    return sum(squared_errors) / len(squared_errors)


def example_simple_tokenizer(text: str) -> list[str]:
    """
    A very basic tokenizer for NLP.
    Converts text to lowercase and splits by whitespace, removing punctuation.
    
    Args:
        text (str): Input sentence.
        
    Returns:
        list[str]: List of tokens.
    """
    # Simple punctuation removal
    clean_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            clean_text += char
            
    return clean_text.lower().split()


if __name__ == "__main__":
    print("--- Dot Product ---")
    inputs = [1.0, 2.0, 3.0]
    weights = [0.5, 0.5, 0.5]
    print(f"Inputs: {inputs}")
    print(f"Weights: {weights}")
    print(f"Dot Product: {example_dot_product(inputs, weights)}")
    
    print("\n--- MSE Loss ---")
    preds = [2.5, 0.0, 2.0]
    actuals = [3.0, -0.5, 2.0]
    print(f"MSE: {example_mean_squared_error(preds, actuals)}")
    
    print("\n--- Tokenization ---")
    sentence = "Hello, AI World! This is Python."
    print(f"Original: {sentence}")
    print(f"Tokens: {example_simple_tokenizer(sentence)}")
