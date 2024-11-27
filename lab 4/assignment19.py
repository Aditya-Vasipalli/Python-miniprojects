import re
def seconds_between():
    total_sec_1=time_1_second + 60*time_1_minute + 60*60*time_1_hour
    total_sec_2=time_2_second+60*time_2_minute+60*60*time_2_hour
    second_diff=total_sec_1-total_sec_2
    return abs(second_diff)
try:
    time_1=input('enter time stamp as hours/minutes/seconds')
    time_2=input('enter time stamp as hours/minutes/seconds')
    time_1_hour, time_1_minute, time_1_second=re.split('/| |,', time_1)
    time_2_hour, time_2_minute, time_2_second=re.split('/| |,', time_2)
    time_1_hour,time_1_minute,time_1_second,time_2_hour,time_2_minute,time_2_second=int(time_1_hour), int(time_1_minute), int(time_1_second), int(time_2_hour), int(time_2_minute), int(time_2_second)
    print(f'there are {seconds_between()} seconds between the two times')
except ValueError:
    print('please enter integers with / or , or space between each value')