"""
Topic: Mean Squared Error (MSE)
"""

def run():
    predictions = [2.5, 0.0, 2.0]
    targets = [3.0, -0.5, 2.0]
    
    print(f"Predictions: {predictions}")
    print(f"Targets:     {targets}")
    
    squared_errors = [(p - t) ** 2 for p, t in zip(predictions, targets)]
    mse = sum(squared_errors) / len(squared_errors)
    
    print(f"MSE Loss: {mse}")

if __name__ == "__main__":
    run()
