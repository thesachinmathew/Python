#convert 1st letter to caps and prnt first letter with dots
s="Let him cook"
words=s.split()
s=[word[0].upper()for word in words]
res = '.'. join(s)
print(res)

#find 1st monday of next month by given date
from datetime import datetime, timedelta
def frst(da):
    date = datetime.strptime(da, '%Y-%m-%d')
    nxtm = date.month % 12 + 1
    nxty = date.year + (date.month // 12)
    nxt = datetime(nxty, nxtm, 1)
    dtm = (7 - nxt.weekday() + 0) % 7
    fm = nxt + timedelta(days=dtm)
    return fm.strftime('%Y-%m-%d')
date_str = '2024-08-05'  
print(frst(da))

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

#min and max
a,b,c=2,5,7
print(max(a,b,c))
print(min(a,b,c))


