#Program to check if two sets have any elements in common
set1={1,2,3,4,5}
set2={2,3,4,6}
set3=set1.intersection(set2) #taking intersection
print(f'there are {len(set3)} elements in common and they are: {set3} ')