#Program to insert and delete from dictionary 

#adding value to dictionary:
def create_dictionary():
    diction = {}
    for i in range(int(input('how many values to add in dictionary: '))):
        key = input('key: ')
        value = input('value: ')
        diction[key] = value
    return diction

#deleting from dictionary:
def deleting_dictionary():
    dictionar= create_dictionary()
    print(dictionar.keys())
    dely = input('enter they key for value you want to delete')
    print('before deleting', dictionar)
    del dictionar[dely]
    print('after deleting:, ', dictionar)

try:
    deleting_dictionary()
except:
    print('enter valid value')