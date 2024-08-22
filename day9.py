#sum of diagonal, coloumns, rows of a matrix
import numpy as np
m = np.array([
    [2, 5, 8],
    [1, 7, 3],
    [4, 6, 9]
])
rs = m.sum(axis=1)
cs = m.sum(axis=0)
ds = np.trace(m)
ads = np.fliplr(m).trace()
print("Matrix:")
print(m)
print("\nSum of each row:")
print(rs)
print("\nSum of each column:")
print(cs)
print("\nSum of the main diagonal:")
print(ds)
print("\nSum of the anti-diagonal:")
print(ads)
 
#display all combinations of letters selecting each letter from a different key in a dictionary
from itertools import product
letter_dict = {
    'key1': ['A', 'B'],
    'key2': ['1', '2'],
    'key3': ['x', 'y']
}
lists_of_letters = letter_dict.values()
combinations = product(*lists_of_letters)
for combination in combinations:
    print(''.join(combination))

#find the largest palindrome made from two 4 digit numbers
def pal(num):
    return str(num) == str(num)[::-1]
def fin(num1, num2):
    product = num1 * num2
    if pal(product):
        return product
    else:
        return None
n = 9999
m = 9901
p = fin(n, m)
if p:
    print(f"The product of {n} and {m} is {p}, which is a palindrome.")
else:
    print(f"The product of {n} and {m} is not a palindrome.")

#find the max total from top to bottom of the triangle 
def m(t):
    dp = [row[:] for row in t]
    for i in range(len(dp) - 2, -1, -1):
        for j in range(len(dp[i])):
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])
    return dp[0][0]
tri = [
    [3],
    [4, 6],
    [2, 7, 6],
    [8, 5, 9, 3]
]
mat = m(tri)
print(f"The maximum total from top to bottom of the triangle is {mat}")

#find the difference between squares of the first 2 natural numbers and square of their sum
def dif(a, b):
    aa = a ** 2
    bb = b ** 2
    s = a + b
    ss = s ** 2
    sss = aa + bb
    d = sss - ss
    return d
    
num1 = 1
num2 = 2
res = dif(num1, num2)
print(f"Difference: {res}")

#check if the given sequence is additive sequence or not
def ad(s):
    n = len(s)
    if n < 3:
        return False
    for i in range(2, n):
        if s[i] != s[i - 1] + s[i - 2]:
            return False
    return True
seq =[1, 2, 3, 5, 8]
res=ad(seq)
if(res==True):
    print("Is additive")
else:
    print("Not additive")
#geometric progression or not
def geo(se):
    n = len(se)
    if n < 3:
        return False
    if se[0] == 0:  
        return False
    r = se[1] / se[0]
    for i in range(2, n):
        if se[i - 1] == 0: 
            return False
        cc = se[i] / se[i - 1]
        if cc != r:
            return False
    return True
s = [2, 6, 18, 54]
result = geo(s)
print(f"The sequence {s} is {'geometric' if result else 'not geometric'}.")

#sum of all multiples of 3 or 5 till a key value
def ss(l):
    tot = 0
    for n in range(l):
        if n % 3 == 0 or n % 5 == 0:
            tot += n
    
    return tot
k = 10
res = ss(k)
print("sum:",res)

#sum of digits
n = input("Enter a string containing digits: ")
d = 0
for char in n:
    if char.isdigit():
        d += int(char)
print("The sum:",d)

#take the sentence as input align justified
def justify_text(sentence, width):
    words = sentence.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) > width:
            lines.append(current_line)
            current_line = []
            current_length = 0
        current_line.append(word)
        current_length += len(word)
    
    if current_line:
        lines.append(current_line)
    
    justified_lines = []
    for line in lines:
        if len(line) == 1:
            justified_lines.append(line[0].ljust(width))
        else:
            total_chars = sum(len(word) for word in line)
            spaces_needed = width - total_chars
            spaces_between_words = spaces_needed // (len(line) - 1)
            extra_spaces = spaces_needed % (len(line) - 1)
            
            justified_line = line[0]
            for i in range(1, len(line)):
                spaces = spaces_between_words + (1 if i <= extra_spaces else 0)
                justified_line += ' ' * spaces + line[i]
                
            justified_lines.append(justified_line)
    
    return '\n'.join(justified_lines)
sentence = input("Enter a sentence to justify: ")

width = int(input("Enter the width for justification: "))

justified_text = justify_text(sentence, width)

print("\nJustified Text:")
print(justified_text)
