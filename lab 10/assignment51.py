#Program to Return a set of elements present in Set A or B, but not both
#declaring sets
set_A, set_B= set(), set()
set_A.update(input('add value to 1st set: ') for i in range(int(input('length of set'))))
set_B.update(input('add value to 2nd set: ') for i in range(int(input('length of set'))))
#checking
set_C=set_A.symmetric_difference(set_B)
print(set_C)