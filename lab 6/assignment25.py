#Program to display first n multiples of a number
try:
    num=float(input('what is the number you need to multiply: '))
    n=int(input('how many multiples'))
except ValueError:
    print('please enter valid number')
for i in range(n+1):
    print(i*num)