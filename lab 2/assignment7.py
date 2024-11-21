#Program to check if a number is positive, negative or 0
def check_number(num):
    if num>0:
        print('number is positive')
    elif num<0:
        print('number is negative')
    elif num==0:
        print("number is 0")
    else:
        print("invalid number")
try:
    check_number(float(input("enter number")))
except ValueError:
    print('please enter a number')
