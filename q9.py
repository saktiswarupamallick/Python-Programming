def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

# Get user input
term_number = int(input("Enter the value of n to find the nth Fibonacci term: "))

# Call the function to find the nth term
result = fibonacci(term_number)

print(f"The {term_number}th term of the Fibonacci sequence is: {result}")
