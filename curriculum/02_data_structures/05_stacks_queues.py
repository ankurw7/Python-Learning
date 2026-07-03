# 05_stacks_queues.py
# Stacks and Queues using Python lists

# --- STACK (Last-In, First-Out) ---
print("--- Stack Demo ---")
stack = []
stack.append("A")
stack.append("B")
stack.append("C")
print(f"Stack: {stack}")

popped = stack.pop()  # Removes 'C'
print(f"Popped: {popped}")
print(f"Stack after pop: {stack}")

# --- QUEUE (First-In, First-Out) ---
from collections import deque

print("\n--- Queue Demo ---")
queue = deque()
queue.append("First")
queue.append("Second")
queue.append("Third")
print(f"Queue: {list(queue)}")

served = queue.popleft()  # Removes 'First'
print(f"Served: {served}")
print(f"Queue after serve: {list(queue)}")
