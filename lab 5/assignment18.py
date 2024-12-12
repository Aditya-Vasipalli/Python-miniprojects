'''
In bowling, the player starts with 10 pins at the far end of a lane. The object is to knock all the pins 
down. For this exercise, the number of pins and balls will vary. Given the number of pins N and 
then the number of balls K to be rolled, followed by K pairs of numbers (one for each ball rolled), 
determine which pins remain standing after all the balls have been rolled. The balls are numbered 
from 1 to N (inclusive) for this situation. The subsequent number pairs, one for each K represent 
the start to stop (inclusive) positions of the pins that were knocked down with each role. Print a 
sequence of N characters, where "I" represents a pin left standing and "." represents a pin knocked 
'''

# Process each ball
def ball():
    for i in range(K):
        print(f"Ball {i + 1}:")
        start = int(input("What position did the first pin get knocked down at: ")) - 1
        end = int(input("What position did the last pin get knocked down at: ")) - 1
        for j in range(start, end + 1):
            pins[j] = 'down'  # Mark pins as knocked down
    # Output final state of pins
    result = "".join(["I" if pin == 1 else "." for pin in pins])
    return result

try: 
# Input the number of pins (N) and the number of balls (K)
    N = int(input("Enter the total number of pins: "))
    K = int(input("Enter the number of balls rolled: "))

    # Create a list of pins (1 = standing, 0 = knocked down)
    pins = ['up'] * N

    print("Final state of the pins:", ball())
except ValueError:
    print('please enter a whole number')
except IndexError:
    print('what')