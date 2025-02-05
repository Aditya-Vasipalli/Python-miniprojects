#Program to display first n Fibonacci numbers

# Function to print first n Fibonacci numbers
def fibbo(n):
    a, b = 0, 1 # Initializing first two Fibonacci numbers
    for _ in range(n):
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b  # Update the values of a and b
try:
    n=int(input('Enter how many fibonacci terms to find: '))
except:
    print('enter a number please')
fibbo(n)