#program to print values of dictionary 
# creating dictionary
def create_dictionary():
    diction = {}
    for i in range(int(input('how many values to add in dictionary: '))):
        key = input('key: ')
        value = input('value: ')
        diction[key] = value
    return diction

# printing values
def val_dictionary():
    diction = create_dictionary()
    for key, value in diction.items():
        print("The Values are: ", value)
    print("also can be shown as: ",list(diction.values()))

try:
    val_dictionary()
except:
    print('enter valid')