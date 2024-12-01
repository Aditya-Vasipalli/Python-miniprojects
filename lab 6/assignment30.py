#Program to access List Index and Values
#first create list:
list1=[]
for i in range(10):
    list1.append(input('enter value to add to list'))
#accessing List:
index=int(input('enter the index you want to access: '))
print('value is: ', list1[index])
