#program to check if number is prime
def check_prime(num):
    value=0
    for i in range(2,num):
        if num%i==0:
            print('number is prime')
            break
        else:
            value=1        
    if value==1:
        print('number is not prime')
try:
    check_prime(int(input('enter the number you want to check for prime: ')))
except ValueError:
    print('please enter valid integer')