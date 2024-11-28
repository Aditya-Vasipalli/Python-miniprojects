try:
    a=float(input('enter coeff of x**2: '))
    b=float(input('enter coeff of x: '))
    c=float(input('enter constant term: '))
except ValueError:
    print('please enter numbers')

#equation = a*x**2+b*x+c
def find_roots(a,b,c):
    disc=(b**2-4*a*c)**(1/2)
    print(disc)
    root_1=(-b-disc)/(2*a)
    root_2=(-b+disc)/(2*a)
    return (root_1,root_2)
print(f'the equation is {a}x**2+ {b}x + {c}')
print('the roots are', find_roots(a,b,c))