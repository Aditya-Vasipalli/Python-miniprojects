#Program to Put Even and Odd elements in a List into Two Different Lists
def odd_even(list):
    even_list, odd_list=[], []
    for i in master_list:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print('Odd list is: ', odd_list)
    print('Even list is: ', even_list)

master_list=[int(input('enter number: ')) for i in range(int(input('how many elements in list: ')))]
odd_even(master_list)