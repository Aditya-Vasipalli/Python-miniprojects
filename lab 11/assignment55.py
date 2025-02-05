#Function to find the maximum of two numbers
def maxx(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return "They are the same number"
    
#calling function:
try:
    num1=int(input('enter 1st number'))
    num2=int(input('enter 2nd number'))
except:
    print('please enter number')
#using function
print(f"bigger number is: {maxx(num1,num2)}")