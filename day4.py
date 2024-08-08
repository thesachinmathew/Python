#convert 1st letter to caps and prnt first letter with dots
s="Let him cook"
words=s.split()
s=[word[0].upper()for word in words]
res = '.'. join(s)
print(res)

#find 1st monday of next month by given date
from datetime import datetime, timedelta
def first_monday_next_month(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    next_month = date.month % 12 + 1
    next_year = date.year + (date.month // 12)
    first_day_next_month = datetime(next_year, next_month, 1)
    days_to_monday = (7 - first_day_next_month.weekday() + 0) % 7
    first_monday = first_day_next_month + timedelta(days=days_to_monday)
    return first_monday.strftime('%Y-%m-%d')
date_str = '2024-08-05'  
print(first_monday_next_month(date_str))

#mean,median.mode
from statistics import mean, median, mode
num=[1,2,3,4,5,6,2]
mean_value= mean(num)
medain_value= median(num)
mode_value= mode(num)
print(f"mean:{mean_value}, median:{medain_value}, mode:{mode_value}")

#n series
def sum_of_series(num):
    result=0
    fact=1
    for i in range(1, num+1):
        fact*=i
        result= result+(fact/i)
    return result
n=5
print("sum:", sum_of_series(n))

#prnt day by given date
import calendar
year,month,day= 2024, 8, 7
day_index= calendar.weekday(year, month, day)
day_name= calendar.day_name[day_index]
print(day_name)





