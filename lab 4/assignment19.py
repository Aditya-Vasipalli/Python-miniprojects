
time_1_hour=int(input('hour 1: '))
time_1_minute=int(input('min 1: '))
time_1_second=int(input('sec 1: '))
time_2_hour=int(input('hour 2: ' ))
time_2_minute=int(input('min 2: '))
time_2_second=int(input('sec 2: '))

time_1='2/10/200'
time_2='1/10/200'
for i in range(len(time_1)):
    if time_1[i]=='/':
        unpack_time_1=0

def seconds_between():
    minute1=60*time_1_minute
    hour1=60*60*time_1_hour
    total_sec_1=time_1_second + minute1 + hour1
    minute2=60*time_2_minute
    hour2=60*60*time_2_hour
    total_sec_2=time_2_second+minute2+hour2
    second_diff=total_sec_1-total_sec_2
    return second_diff
print(f'there are {seconds_between()} seconds between the 2 time')
