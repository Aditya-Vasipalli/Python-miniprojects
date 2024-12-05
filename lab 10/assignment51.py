#Program to Return a set of elements present in Set A or B, but not both
#declaring sets
set_A={1,2,3,4}
set_B={3,4,5,6}
#checking
set_C=set_A.symmetric_difference(set_B)
print(set_C)