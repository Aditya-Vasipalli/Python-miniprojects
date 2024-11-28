#Program to check if a date is valid
import re

def leap_year(year):
    if year%100==0:
        if year%400==0:
            return leap
        else:
            return not leap
    elif year%4==0:
        return leap
    else:
        return not leap

def valid_date():
    date=input('enter date in dd/mm/yyyy format: ')
    day, month, year=re.split('/| |-|,',date)
    day=int(day)
    month=int(month)
    year=int(year)
    if day and month and year >0:
        if month <=12:
            if month in [1,3,5,7,8,10,12] and day<=31:
                return 'valid'
            elif month in [4,6,9,11] and day<=30:
                return 'valid'
            elif month==2:
                leap_year(year)
                if leap is True and day<=29:
                    return 'valid'
                elif leap is False and day <=28:
                    return 'valid'
                else:
                    return 'invalid'
        else:
            return 'invalid'    
    else:
        return 'invalid'

try:
    leap=True
    print('date is', valid_date())
except ValueError:
    print('please enter date as integer values with /,- or space between them')