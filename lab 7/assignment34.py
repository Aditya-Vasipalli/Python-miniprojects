#Program to Find the Second Largest Number in a List 

list1=[float(input('please enter number: ')) for i in range(int(input('how many elements in list: ')))]
def find_value():
    value=max(list1)
    index=0
    for i in list1:
        if i==value:
            return index
        index+=1

def second_largest():
    list1.pop(find_value())
    return max(list1)

print(f'The second largest value is: {second_largest()}')
        