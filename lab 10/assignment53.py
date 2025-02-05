#Program to Remove items from set1 that are not common to both set1 and set2 
set1, set2 = set(), set()
set1.update(input('add value to 1st set: ') for i in range(int(input('length of set'))))
set2.update(input('add value to 2nd set: ') for i in range(int(input('length of set'))))
set1=set1.intersection(set2) #new set 1 has only elements common in both
print(set1)