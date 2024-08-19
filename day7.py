#binary addition
a,b= '1010', '1101'
result= bin(int(a,2)+int(b,2))[2:]
print(result)


#Create frequency of elements in list
from collections import Counter
lst=[1,2,2,3,3,3]
freq= Counter(lst)
print(freq)


#matrix multiplication
import numpy as np
A= np.array([[1,2], [3,4]])
B= np.array([[5,6], [7,8]])
result= np.dot(A,B)
print(result)

#starting & ending of target in list
lst = [1, 2, 3, 2, 4, 2, 5]
target = 2

start = -1
end = -1
for i, num in enumerate(lst):
    if num == target:
        if start == -1:
            start = i
        end = i

print(start, end) 


#string is valid or not
def is_valid_brackets(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack == [] or bracket_map[char] != stack.pop():
                return False
        else:
            continue
    return stack == []
print(is_valid_brackets("()"))       
print(is_valid_brackets("()[]{}"))  
print(is_valid_brackets("(]"))        
print(is_valid_brackets("([)]"))      
print(is_valid_brackets("{[]}"))     

#string operation
s1= "hello"
s2= "world"
s3= ''.join(a+b for a,b in zip(s1,s2)) 
print(s3)


#strings needle and hashtag
def find_index(needle, hashtag):
    last_char = hashtag[-1]
    index = needle.find(last_char)  
    return index
needle = "NEEDLE"
hashtag = "HASHTAG"
index = find_index(needle, hashtag)
print(f"The index of the first occurrence of '{hashtag[-1]}' in '{needle}' is: {index}")

#two strings are isomorphic or not
def is_isomorphic(s,t):
    return len(set(zip(s,t)))==len(set(s))==len(set(t))
print(is_isomorphic('paper', 'tittle'))
print(is_isomorphic('foo', 'bar'))

#upper and lower until star
input_data= []
while True:
    user_input = input("enter a letter or number(or '*' to stop): ")
    if user_input == '*':
        break
    input_data.append(user_input)
print("you entered:", input_data)

#vowels lexiographically sorted
from itertools import product 
n=2
vowels='aeiou'
result= [''.join(p) for p in product(vowels, repeat=n)]
print(result)
