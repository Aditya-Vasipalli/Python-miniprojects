#Program to find the sum of digits of a number
try:
    num=input('enter a number you want sum of digits of: ')
    sum=0
    for i in num:
        sum=sum+int(i)
    print(f'sum of digits is: {sum}')
except ValueError:
    print('please enter a integer')