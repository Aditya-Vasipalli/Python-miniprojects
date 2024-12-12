# Program to display first n numbers
def first_n_numbers(n):
    for i in range(n+1):
        print(i)
try:
    first_n_numbers(int(input('enter n to print first n numbers: ')))
except ValueError:
    print('please enter an integer')