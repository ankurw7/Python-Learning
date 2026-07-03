# 04_while_loops.py
# Example: Using a while loop to count down

count = 5
print("Countdown starting...")

while count > 0:
    print(count)
    count -= 1

print("Blast off!")

# Example: Using break to exit a loop
print("\nLooking for the number 3...")
n = 0
while True:
    print(f"Checking {n}...")
    if n == 3:
        print("Found 3! Exiting loop.")
        break
    n += 1
