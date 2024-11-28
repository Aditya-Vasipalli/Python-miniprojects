#Given a string. Delete from it all the characters whose indices are divisible by 3. 
string=input('enter a string: ')
new_string=''
for i in range(len(string)):
    if i%3!=0:
        new_string+=string[i]
print(new_string)
