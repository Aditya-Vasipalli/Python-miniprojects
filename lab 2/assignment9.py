# Problem 9 : Angle of the Hour Hand 
''' 
Ask user to enter the time and find whats the angle of the hour hand (Taas Kata) with respect to 12 o'clock.
There are 12 hours and 360 degree circle and thus each hour represents 30 degrees (360/12).
Find the exact number of hours and get the angle. 
'''
def angle():
    Time_in_hour = H + M /60 + S/3600
    Angle = Time_in_hour * 30
    return Angle
try:
    H = int(input("Enter Hours between 0 to 12 : "))
    M = int(input("Enter Minutes between 0 to 60 : "))
    S = int(input("Enter Seconds between o to 60 : "))
except ValueError():
    print('please enter an integer')

print("Angle is : ", angle() ," Degrees") 