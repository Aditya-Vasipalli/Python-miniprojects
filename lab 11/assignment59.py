#Function to Find the Sum of the Digits of the Number Recursively
def summ(n):
    if n==0:
        return 0
    else:
        return n+summ(n-1)
    
imput=int()