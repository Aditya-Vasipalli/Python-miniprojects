#Program to check whether a given key already exists in a dictionar

diction={ #declaring dictionary
    "name1": "Aria",
    "age1": 19,
    "place1": "london",
    "name2": "Emily",
    "age2": 21,
    "place3": "New york",
}
#checking
check=input("check which key: ")
if check in diction.keys():
    print('key is already in dictionary')
else:
    print('key is not in dictionary')