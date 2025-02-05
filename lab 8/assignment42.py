#Program to print all keys of dictionary

#creating dictionary
def create_dictionary():
    diction = {}
    for i in range(int(input('how many values to add in dictionary: '))):
        key = input('key: ')
        value = input('value: ')
        diction[key] = value
    return diction
#printing all keys
dicty= create_dictionary()
print(list(dicty.keys()))