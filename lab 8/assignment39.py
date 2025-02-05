#Program to create and view a dictionary

# creating dictionary
def create_dictionary():
    dictionion = {}
    for i in range(int(input('how many values to add in dictionary: '))):
        key = input('key: ')
        value = input('value: ')
        dictionion[key] = value
    return dictionion

#view dictionary:
dictionar= create_dictionary()
print('elements of dictionary are:', dictionar, type(dictionar))