#Given a sequence of integer numbers ending with the number 0. Determine the length of the widest fragment where all the elements are equal to each other

def widest_fragment(num):
    count=1
    max_count=1
    for i in range(1,len(num)):
        if num[i]==num[i-1]:
            count+=1
        else:
            if count>max_count:
                max_count=count
            count=1
    return max_count
num=str(input('num'))
print(f'the widest fragment is {widest_fragment(num)} long')