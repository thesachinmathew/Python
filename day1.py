#1 right triangle
r=5
for i in range(1,r+1):
  print(" "*(r-i)+"*"*i)

#2 left triangle
r=5
for i in range(i,r+1):
  print("*"*i+(r-1)*" ")

#3 remove duplicate
l=[1,2,3,4,5,2,2,1,2,3]
print(list(set(l)))

#4 count duplicates
l=[1,2,2,3,2,1,2,3,2,1,1]
b={}
for i in l:
  if i in b:
    b[i]+=1
  else:
    b[i]=1
for k,v in b.i():
  if(v>1):
    print(f"{k} appears {v} times")

#5 +ve -ve sum
n=0
p=0
k=[1,2,3,-4,-3,-7,4,-6]
for i in range(0,7):
  if(k[i]<0):
    n=n+k[i]
  else:
    p=p+k[i]
print("Positive sum:",p,"\nNegative sum:",n)

#6 tech number
n=3025
l=len(str(n))
if l%2==0:
  if(int (str(n){l//2:})+int(str(n){l//s}))**2==n:
    print("Tech no")

#7 prime or composite
n=7
if(n%2==0 and n!=2 or n%3==0 and n!=3 or n%5==0 and n!=5 and n%1!=0 and n!=1):
  print("It is not prime")
else:
  print("It is prime")

#8 alpha unicode
for char in range(ord('a'),ord('z')+1):
  print(chr(char),char)

#9 perfect
n=30
s=0
for i in range(1,n):
  if(n%i==0):
    s+=i
  if(s==n):
    print(n,"is perfect")
  else:
    print(n,"Not perfect")

#10 upper, lower, count words, count words with a first letter
s="apples can grow out of BANANAS"
print("Upper case:",s.upper())
print("lower case:",s.lower())
print("num of words:",(s.split()))
t=s.split()
ca=0
for w in t:
  if w.startswith('a'):
    ca+=1
print("Number of words starting with 'a':", ca)





