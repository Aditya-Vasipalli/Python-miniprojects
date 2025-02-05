newstring=""
oldstring="0123456789"
for i in range(0, len(oldstring)):
    if i/3!=0:
        print(i)
        newstring=newstring+oldstring[i]
print(newstring)