#Program 48. Program to Get the Maximum and Minimum Value in a Dictionary
#creating dictionary
def create_dictionary():
    diction = {}
    for i in range(int(input('how many values to add in dictionary: '))):
        key = input('key: ')
        value = int(input('enter number values(for max/min):  '))
        diction[key] = value
    return diction

try:
    funky_dict=create_dictionary()
except:
    print('enter valid value')


# Get the maximum score
max_score = max(funky_dict.values())
print("Maximum score:", max_score)

# Get the minimum score
min_score = min(funky_dict.values())
print("Minimum score:", min_score)
