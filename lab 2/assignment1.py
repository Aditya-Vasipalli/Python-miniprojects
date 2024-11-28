pi=22/7 #constant value of pi
def area_of_circle(r):
    area=pi*r**2
    print("area of circle is:", area)

def area_of_triange(base, height):
    area=(1/2)*base*height
    print("area of triangle is:", area,"\n")


if __name__ == '__main__':
    while True:
        opt=input(("\nfind area of :\n1.Circle\n2.Triangle\n3.Exit\nSelect from 1,2,3\n"))
        if opt=='1':
            area_of_circle(float(input('enter radius: ')))
            print("***************************************************************")
        elif opt=='2':
            base=float(input('enter length of base: '))
            height=float(input('enter length of height: '))
            print("***************************************************************")
            area_of_triange(base, height)
        elif opt=="3":
            break
        else:
            print('select valid option')