#lcm and gcd
import math
n=2
m=4
print("GCD:",math.gcd(n,m))
print("LCM:",(n*m)/math.gcd(n,m))

#len of last word
s="your throat has a goat tied on the decks"
w=s.split()
print("Length of last word is",len(w[-1])

#composite num
a=10
b=30
c=0
for n in range(a,b):
    if(n%2==0 and n!=2 or n%3==0 and n!=3 or n%5==0 and n!=5):
        print(n)

#sqr,cube,sqrt
import math
n=4
square=n**2
cube=n**3
square_root=math.sqrt(n)
print(square,cube,square_root)

#combinatiomns
import itertools
num=[1,2,3]
for perm in itertools.permutations(num):
    print(perm)

#leap year
year=2000
is_leap= year%4==0 and (year%100==0 or year%400==0)
print("leap year" if is_leap else "not an leap year")

#len of last word
s="got a stalker walking up and down the street"
length= len(s.split()[-1])
print(length)

#palindrome
n=123
is_palindrome= str(n)==str(n)[::-1]
print("palindrome" if is_palindrome else "not an palindrome")

#prime btw 2 nums
a=10
b=30
c=0
for n in range(a,b):
    if(n%2==0 and n!=2 or n%3==0 and n!=3 or n%5==0 and n!=5 or n==1):
        c=1
    else:
        print(n)

#sum od series
num = 5
print(sum([i**2 for i in range(1, num+1)]))

#sum of odd and even
num=[1,2,3,4,5]
sum_even=sum(x**2 for x in num if x%2==0)
sum_odd=sum(x**2 for x in num if x%2!=0)
print("even", sum_even,"odd", sum_odd)
