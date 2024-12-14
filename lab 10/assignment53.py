#Program to Remove items from set1 that are not common to both set1 and set2 
set1={1,2,3,4,5}
set2={2,3,4,6}
set1=set1.intersection(set2) #new set 1 has only elements common in both
print(set1)