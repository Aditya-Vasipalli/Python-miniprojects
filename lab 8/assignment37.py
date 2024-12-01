#Program to Generate Random Numbers from 1 to 20 and Append Them to the List
import random
list_range=int(input('enter number of elements in list: '))
list_random=[]
#appending to the list:
for i in range(list_range):
    list_random.append(random.randint(1,20))
print(list_random)