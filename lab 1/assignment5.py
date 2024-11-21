def using_inbuilt(a,b):
    max_num=max(a,b)
    print(max_num, 'is max')

def using_ifelse(a,b):
    if a>b:
        print(a, 'is max')
    elif b<a:
        print(b, 'is max')
    elif a==b:
        print('same number')
    else:
        pass

try:
    a=int(input('enter number'))
    b=int(input('enter second number'))
    using_ifelse(a,b)
    using_inbuilt(a,b)
except ValueError:
    print('please enter a number')