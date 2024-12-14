#Function to check if a number is even or odd 
def oddoreven(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
try:
    print('the number is: ',oddoreven(int(input('enter number to check'))))
except ValueError:
    print('enter a number')