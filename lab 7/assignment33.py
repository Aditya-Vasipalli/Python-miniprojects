#Program to Find the Largest Number in a List
try:
    list1=[float(input('please enter number: ')) for i in range(int(input('how many elements in list: ')))]
    print(f'The largest number in the list is: {max(list1)}')
except ValueError:
    print("enter a valid number")