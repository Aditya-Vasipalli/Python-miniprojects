#Program to merge two Python dictionaries
# creating first dictionary
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

# Merging dictionaries using update() method
try:
    first_dict = first_dictionary()
    second_dict = second_dictionary()
    merged_dict=first_dict.copy()
    merged_dict.update(second_dict)
    print("Merged dictionary using update():", merged_dict)
except:
    print('enter valid value')