#Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10

def perfect_square(list_num):
    for num in list_num:
        count=0
        for j in str(num):
            count=count+int(j)
        if count>10:
            pass
        else:
            for i in range(n):
                if i**2==num:
                    print(f'{num} is a perfect square and sum of digits is less than 10')
try:
    n=int(input('enter range: '))
    perfect_square([i for i in range(n)])
except ValueError:
    print('please enter an integer for range')