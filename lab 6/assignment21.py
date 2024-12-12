#Program to calculate factorial of a number
def factorial(num):
    ans=1
    for i in range(1,num+1):
       ans=ans*i
    print(ans)
try:
    factorial(int(input('find factorial of?: ')))
except ValueError:
    print('enter integer')