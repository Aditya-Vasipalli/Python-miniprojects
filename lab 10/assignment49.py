#Program 49. Program to Add a List of Elements to a Set
try:
    # Initial set
    og_set = set()
    og_set.update(input('add value to og set: ') for i in range(int(input('length of set'))))

    # List to add
    list_to_add = [input('enter element: ') for i in range(int(input('enter how many elements in list: ')))]

    # Add list elements to the set
    og_set.update(list_to_add)
    print("Updated set:", og_set)
except:
    print('please enter valid value')