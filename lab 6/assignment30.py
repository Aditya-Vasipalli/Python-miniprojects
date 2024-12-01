#Program to access List Index and Values
#first create list:
list1=[input('enter values in list' for i in range(10))]
#accessing List:
index=int(input('enter the index you want to access: '))
print('value is: ', list1[index])

#accessing index:
value=input('enter value to check index of: ')
index=0
for i in list1:
    index+=1
    if i==value:
        print('found at index', index)