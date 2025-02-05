#Program 50. Program to Update the First Set with Items That Don’t Exist in the Second Set
# Initial set
set1, set2 = set(), set()
set1.update(input('add value to 1st set: ') for i in range(int(input('length of set'))))
set2.update(input('add value to 2nd set: ') for i in range(int(input('length of set'))))



# Update test_players with items not in t20_players
set1.difference_update(set2)
print("updated values after removing common elements:", set1)
