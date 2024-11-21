#Given integer coordinates of three vertices of a rectangle whose sides are parallel to the coordinate axes, find the coordinates of the fourth vertex of the rectangle. In the first test the three given vertices are (1, 4), (1, 6), (7, 4). The fourth vertex is thus (7, 6).


def missing_coord(coord1, coord2, coord3):
    if coord1==coord2==coord3:
        pass
    elif coord1==coord2:
        return coord3
    elif coord1==coord3:
        return coord2
    elif coord2==coord3:
        return coord1
    else:
        pass

print('Enter the coordinates of the three vertices of the rectangle in order of ABC to find coordinates of D:')
try:
    A=[int(input('Enter x for A: ')),int(input('Enter y for A: '))]
    B=[int(input('Enter x for B: ')),int(input('Enter y for B: '))]
    C=[int(input('Enter x for C: ')),int(input('Enter y for C: '))]
except ValueError: 
    print('please enter integer')
x= missing_coord(A[0], B[0], C[0])
y= missing_coord(A[1], B[1], C[1])
D=(x,y)
if x and y==None:
    print('The coordinates are not of a rectangle')
else:
    print('The coordinates of D are:',D)