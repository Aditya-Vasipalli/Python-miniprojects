#Given a sequence of integer numbers ending with the number 0. Determine the length of the widest fragment where all the elements are equal to each other

def widest_fragment(list_of_number):
    count=1
    max_count=1
    answ=''
    for i in range(1,len(num_list)):
        if num_list[i]==num_list[i-1]:
            count+=1
        else:
            if count>max_count:
                max_count=count
                answ=num_list[i-1]
            count=1
    print(f'the widest fragment is {max_count} long')
    return answ
num_list=[]

while True:
    num=str(input('enter number (or 0 to stop)'))
    num_list.append(num)
    if num=='0':
        print('widest fragment is: ', widest_fragment(num_list))        
        break