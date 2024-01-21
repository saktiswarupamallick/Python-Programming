def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function to find the GCD
gcd_result = find_gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {gcd_result}")
