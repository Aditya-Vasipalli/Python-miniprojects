#Program to sort (ascending and descending) a dictionary by value 
#creating dictionary
def create_dictionary():
    diction = {}
    for i in range(int(input('how many values to add in dictionary: '))):
        key = input('key: ')
        value = int(input('enter number values(for sorting):  '))
        diction[key] = value
    return diction

try:
    new_dictionary= create_dictionary()
except:
    print('please enter valid value')

# Sorting in ascending order by value 

ascending_scores = dict(sorted(new_dictionary.items(), key=lambda item: item[1]))
print("Sorted in ascending order by value:", ascending_scores)

# Sorting in descending order by value
descending_scores = dict(sorted(new_dictionary.items(), key=lambda item: item[1], reverse=True))
print("Sorted in descending order by value:", descending_scores)

