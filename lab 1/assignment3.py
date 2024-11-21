import random
rando=random.randint(0,100)
random_times=eval(input("how many chances do you need to guess an integer between 0 and 100\nchoose less than 10 chances:"))
if random_times<=10:
    for i in range(1,random_times+1):
        guess=int(input('guess'))
        print("guess number:", i)
        if guess==rando:
            print("you guessed it right")
        chance=i
        if i==random_times:
            print('it was', rando)

else: 
    pass
random_fraction=random.random()
print('here is a random fraction:', random_fraction)