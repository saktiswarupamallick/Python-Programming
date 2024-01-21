def reverse_number(num):
    # Convert the number to a string for easy reversal
    num_str = str(num)
    
    # Reverse the string
    reversed_str = num_str[::-1]
    
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)
    
    return reversed_num

# Get user input
number = int(input("Enter a number to find its reverse: "))

# Call the function to find the reverse
result = reverse_number(number)

print(f"The reverse of {number} is: {result}")
