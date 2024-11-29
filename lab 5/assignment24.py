#Program to calculate sum and average of first n numbers 

def sum(n):
    total=0
    for i in range(n+1):
        total=total+i
    return total
def average(n):
    total=sum(n)/n
    return total
try: 
    n=int(input('enter the nth number: '))
    print('average is', average(n), 'and sum is', sum(n))
except ValueError:
    print('please enter integer')