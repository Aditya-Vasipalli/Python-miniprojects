#Program to display numbers in the reverse order
def rev_num(num):
    for i in range(num,-1,-1):
        print(i)
try:
    rev_num(int(input('enter the number to start from: ')))
except ValueError:
    print('enter integer')