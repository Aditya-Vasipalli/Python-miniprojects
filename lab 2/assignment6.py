def odd_even(number):
    if number%2==0:
        print('even number')
    else:
        print('odd number')
try:
    odd_even(int(input('enter integer')))
except ValueError:
    print('please enter an integer ')