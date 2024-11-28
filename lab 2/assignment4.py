def km_to_mile(km):
    mile=km*1.609344
    print(mile)
def mile_to_km(mile):
    km=mile*0.621
    print(km)
try:
    typeconvert=input('1. Mile to kilometer\n2. Kilometer to mile')
    if typeconvert=='1':
        print(mile_to_km(float(input('enter how many miles'))))
    if typeconvert=='2':
        print(km_to_mile(float(input('enter how many miles'))))
except ValueError:
    print('please enter a number')