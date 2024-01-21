def list_sum(lst):
    # Base case: an empty list has a sum of 0
    if not lst:
        return 0
    else:
        # Recursive case: sum the first element with the sum of the rest of the list
        return lst[0] + list_sum(lst[1:])

# Get user input for the list
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input to a list of integers
numbers = [int(x) for x in user_input.split()]

# Call the function to find the sum
result = list_sum(numbers)

print(f"The sum of the elements in the list is: {result}")

