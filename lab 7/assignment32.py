#Program to check if a List is Empty or Not
try:
    list1=[input('enter value for list: ') for i in range(int(input('enter how many elements in list: ')))]
    x= 'Empty' if len(list1)==0 else 'Not empty'
    print(f'list is {x} and has {len(list1)} elements')
except ValueError:
    print('please enter an integer value')