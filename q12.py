import copy

# Original list
original_list = [1, 2, [3, 4], 5]

# Create a deep copy using copy.deepcopy()
deep_copy = copy.deepcopy(original_list)

# Modify the deep copy to demonstrate its deep nature
deep_copy[2][0] = 'Y'

# Print both the original and the deep copy
print("Original List:", original_list)
print("Deep Copy:", deep_copy)
