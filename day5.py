#automorphic
n=25
print(srt(n**2).endswith(str(n)))

#fibonacci triangle
n=5
a,b= 0,1
for i in range(n):
  for _ in range(i+1):
    print(a, end=' ')
    a,b = b, a+b
    print()

#hollow pyramid
n=10
for i in range(n):
  for j in range(n-i):
    print(' ', end='')

  for j in range(2*i+1):
    if j==0 or j==2*i or i==n-1:
      print('*', end='')
    else:
      print(' ', end='')
  print()

#harshad number
n=18
print(n%sum(int(digit)for digit in str(n))==0)

#number pattern triangle
n=5
for i in range(1, n+1):
  print(' '.join(Str(j)for j in range(1, i+1)))

#perfect number
from math import sqrt
n=16
print(sqrt(n)*sqrt(n)==n)

#smith number
def smth(n):
    s = lambda x: sum(int(d) for d in str(x))
    f, d, fa = n, 2, []
    while d * d <= f:
        while f % d == 0:
            fa.append(d)
            f //= d
        d += 1
    if f > 1: fa.append(f)
    return len(fctors) > 1 and s(n) == sum(map(s, fa))
num = 666
print(smth(num)) 

#strong number
import math
def strg(n):
  return n== sum(math.factorial(int(digit))for digit in str(n))
  n=145
  print(strg(n))

#sum of digits in until single
n=9865
while n>9:
  n=sum(int(digit) for digit in str(n))
  print(n)
