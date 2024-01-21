import copy

# Original list
original_list = [1, 2, [3, 4], 5]

# Create a shallow copy using copy.copy()
shallow_copy = copy.copy(original_list)

# Modify the shallow copy to demonstrate its shallow nature
shallow_copy[2][0] = 'X'

# Print both the original and the shallow copy
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
