try:
    num1=float(input('enter number 1: '))
    num2=float(input('enter number 2: '))
    num3=float(input('enter number 3: '))
except ValueError:
    print('enter  a number please')
print('finding max using function:', max(num1,num2,num3))
def conditional_statements():
    if num1==num2==num3:
        return 'same number'
    elif num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    elif num2>num1:
        if num2>num3:
            return num2
        else:
            return num3

print('finding max of number using conditional statements:', conditional_statements())