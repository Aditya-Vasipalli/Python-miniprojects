# Function with default arguments

def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

# Calling the function with and without default arguments
greet("Alice")
greet("Bob", "Hi")
greet("Charlie", "Good morning", ".")