#Program to insert and delete from dictionary 

#adding value to dictionary:
dictionar={
    
}
try:
    dictionar['name']=input('enter name: ')
    dictionar['age']=int(input('enter name: ' ))
    dictionar['place']=input('enter location: ')
except ValueError:
    print('add valid value')

#deleting from dictionary:
print('before deleting', dictionar)
del dictionar['age']
print('after deleting:, ', dictionar)
