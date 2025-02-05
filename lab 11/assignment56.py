# Function with keyword arguments

def salutations(name, salut="Welcome!", punctuation="!", times=1):
    for _ in range(times):
        print(f"{salut}, {name}{punctuation}")

# Calling the function with various keyword arguments
salutations(name="Alice", salut="Hello", punctuation=".", times=3)
salutations(name="Bob", times=2)
salutations(salut="Greetings", name="Charlie")
salutations(name="Diana")