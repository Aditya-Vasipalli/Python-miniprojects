#Program to access List Index and Values
try:
    #creating list:
    list1=[input('enter values in list') for i in range(10)]
    #accessing List:
    index=int(input('enter the index you want to access: '))
    print('value is: ', list1[index])

    #accessing index:
    value=input('enter value to check index of: ')
    index=0
    for i in list1:
        if i==value:
            print('found at index', index)
        index+=1
except ValueError:
    print('enter valid number')
except IndexError:
    print('please enter index in range')