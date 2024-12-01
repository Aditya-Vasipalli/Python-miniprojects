#Program to Remove the Duplicate Items from a List

def del_dupli():
    for element in dupy_list:
        if element not in new_list:
            new_list.append(element)
    return new_list
try:
    dupy_list=[input('enter element: ') for i in range(int(input('enter how many elements in list: ')))]
    new_list=[]
    print(f'Original list: {dupy_list}')
    print(f'New list: {del_dupli()}')
except ValueError:
    print('enter valid number')