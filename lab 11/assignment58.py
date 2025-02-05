# Function to Find the Factorial of a Number Using Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    # Recursion
    else:
        return n * factorial(n - 1)

# Test the function
number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")