# 04_activation_functions.py
import math

def relu(x):
    """ReLU (Rectified Linear Unit): Returns x if x > 0, else 0"""
    return max(0, x)

def sigmoid(x):
    """Sigmoid: Squashes values between 0 and 1"""
    # math.exp(-x) can overflow for large negative x, so we clip it ideally,
    # but for this simple demo let's keep it raw or handle potential overflow simply.
    if x < -700: # approximation to avoid overflow
        return 0
    return 1 / (1 + math.exp(-x))

print(f"ReLU(5) = {relu(5)}")
print(f"ReLU(-5) = {relu(-5)}")

print(f"Sigmoid(0) = {sigmoid(0)}")
print(f"Sigmoid(10) = {sigmoid(10):.4f}")
print(f"Sigmoid(-10) = {sigmoid(-10):.4f}")
