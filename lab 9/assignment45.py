
#Program 45. Program to Concatenate Dictionaries to Create a New One
# creating dictionary
def first_dictionary():
    diction = {}
    for i in range(int(input('how many values to add in dictionary: '))):
        key = input('key: ')
        value = input('value: ')
        diction[key] = value
    return diction
# creating 2nd dictionary
def second_dictionary():
    diction = {}
    for i in range(int(input('how many values to add in dictionary: '))):
        key = input('key: ')
        value = input('value: ')
        diction[key] = value
    return diction
# Concatenating dictionaries
big_dict = {**first_dictionary(), **second_dictionary()}
print("Combined values from two dictionary:", big_dict)
