try:
    a=float(input('enter coeff of x**2: '))
    b=float(input('enter coeff of x: '))
    c=float(input('enter constant term: '))
except ValueError:
    print('please enter numbers')

#equation = a*x**2+b*x+c
def find_roots(a,b,c):
    disc=(b**2-4*a*c)
    root_1=(-b-disc**(1/2))/(2*a)
    root_2=(-b+disc**(1/2))/(2*a)
    if disc<0:
        print('the roots are imaginary ', root_1, root_2)
    elif disc>0:
        print('the roots are real ', root_1, root_2)
    else:
        print('roots are equal')
print(f'the equation is {a}x**2+ {b}x + {c}')
find_roots(a,b,c)
