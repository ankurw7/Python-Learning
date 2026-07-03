# 06_one_hot_encoding.py

categories = ["cat", "dog", "bird"]
data = ["dog", "cat", "bird", "dog"]

print(f"Categories: {categories}")
print(f"Data: {data}")

# Create a mapping from category to index
cat_to_index = {cat: i for i, cat in enumerate(categories)}

print("\nOne-Hot Encoded Data:")
for item in data:
    # Create a vector of zeros
    vector = [0] * len(categories)
    # Set the index of the current category to 1
    index = cat_to_index[item]
    vector[index] = 1
    
    print(f"{item}: {vector}")
