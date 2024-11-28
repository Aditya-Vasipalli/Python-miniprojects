#A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased. The program should read three integers: the number of students in each of the three classes, a, b and c respectively. In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks is also enough for the third group of 22 students. So we need 32 desks in total.

def total_desks():
    student_class_a=int(input('Number of students in class A: '))
    student_class_b=int(input('Number of students in class B: '))
    student_class_c=int(input('Number of students in class C: '))
    total_students=student_class_a+student_class_b+student_class_c
    if total_students%2==0:
        desk=total_students//2
    else:
        desk=(total_students+1)//2
    return desk
try:
    print('total number of desks required:',total_desks())
except ValueError:
    print('please enter a number')