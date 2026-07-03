# 05_gradient_descent_step.py

# A simple example: trying to move 'w' closer to 'target'
# Loss = (w - target)^2
# Gradient (derivative of Loss with respect to w) = 2 * (w - target)

w = 10.0
target = 2.0
learning_rate = 0.1

print(f"Initial Weight: {w}")
print(f"Target: {target}")

for step in range(5):
    # Calculate Gradient
    gradient = 2 * (w - target)
    
    # Update Weight
    w = w - (learning_rate * gradient)
    
    print(f"Step {step+1}: Gradient = {gradient:.2f}, New Weight = {w:.2f}")

print("Notice how the weight gets closer to the target (2.0) with each step!")
