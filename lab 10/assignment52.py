#Program to check if two sets have any elements in common
set1, set2 = set(), set()
set1.update(input('add value to 1st set: ') for i in range(int(input('length of set'))))
set2.update(input('add value to 2nd set: ') for i in range(int(input('length of set'))))
set3=set1.intersection(set2) #taking intersection
print(f'there are {len(set3)} elements in common and they are: {set3} ')