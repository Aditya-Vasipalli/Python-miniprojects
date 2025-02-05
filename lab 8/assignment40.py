#Program to create and view elements of a set
#Creating set
new_set=set()
for i in range(int(input('how many elements to add: '))):
    new_set.update(input('enter element: '))

#viewing set
print('set is: ', new_set, type(new_set))