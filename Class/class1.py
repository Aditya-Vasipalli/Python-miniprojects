import random
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

#print('hello word')
def check_age():
    name=input('your name')
    age=int(input('your age'))
    print('Namaste', name , 'your age is', age)
    if age<18:
        print('you are underage')
    else:
        print('an adult')

def calculator(a,b):
    c=0
    calc=input('which operation')
    for i in calc:
        if i=='+':
            c=a+b
        elif i=='-':
            c=a-b
        elif i=='*':
            c=a*b
        elif i=='/':
            if b!=0:
                c=a/b
    print(c)

#check_age()
''' calc function run
for i in range(int(input('how many times to calculate:'))):
    calculator(int(input('no1')), int(input('no2')))
'''

'''hello world loop
for i in range(5):
    print('hello world')
'''

def guessing_game():
    random_int=random.randint(0,10)
    print('guess the no between 0 to 10, you have 5 chances')
    for i in range(5):
        guess=int(input('guess no'))
        if guess==random_int:
            print('you got it!')
            break
    print('number was', random_int)
#guessing_game()

def fest():
    festivals=[]
    print('5 festivals you must')
    for i in range(5):
        app_fest=input('enter festival')
        festivals.append(app_fest)
    ret=int(input('which one would you like to access from 1 to 5?'))
    print(festivals[ret-1])
#fest()

def show_array():
    prime_num=np.array([1,2,3,5,7,11,13])
    print('the array one is ', prime_num)
# show_array()

def matplot():
    x=[1,12,13,16,13,12,1]
    y=[13,1,12,16,13,1,12]
    plt.plot(x,y)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.show()
#matplot()

def url():
    url="https://www.kaggle.com/datasets/kishan305/whats-trending-google-india"
    filename='downloaded_data.csv'
    urllib.request.urlretrieve(url, filename)
    print('done')
#url()