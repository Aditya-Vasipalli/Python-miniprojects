#Program to check whether a given key already exists in a dictionary

# creating dictionary
def create_dictionary():
    diction = {}
    for i in range(int(input('how many values to add in dictionary: '))):
        key = input('key: ')
        value = input('value: ')
        diction[key] = value
    return diction
#checking
try: 
    diction=create_dictionary()
    check=input("check which key: ")
    if check in diction.keys():
        print('key is already in dictionary')
    else:
        print('key is not in dictionary')
except:
    print('enter valid value')