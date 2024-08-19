#encode message in alphabets
def encode(message, shift):
    return ''.join(chr((ord(c) - ord('a') + shift) % 26 + ord('a')) if c.islower() else
                   chr((ord(c) - ord('A') + shift) % 26 + ord('A')) if c.isupper() else c
                   for c in message)
print(encode("Hello World", 3))  

#group anagrams from the list of strings
from collections import defaultdict
words = ["eat", "tan", "ate", "nat", "bat", "tea"]
anagrams = defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)
for group in anagrams.values():
    if len(group) > 1:
        print(group)

#isogram
def is_isogram(word):
    word = word.lower()
    return len(word) == len(set(word))
print(is_isogram("Machine")) 
print(is_isogram("Programming"))  

#merge two sorted list
lis1=[1,6,3,2,5,4]
lis2=[11,8,10,7,9]
lis1.sort()
lis2.sort()
print(lis1, lis2)
merged=lis1+lis2
print(merged)

#missing letters which makes it pangram
import string
sentence = "The quick brown fox"
missing_letters = set(string.ascii_lowercase) - set(sentence.lower())
print(''.join(sorted(missing_letters)))  

#pair of elements adds up to give target element
lst = [1, 2, 3, 4, 5, 6]
target = 7
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            print((lst[i], lst[j]))

#pangram
import string
def is_pangram(sentence):
    return set(string.ascii_lowercase) <= set(sentence.lower())
print(is_pangram("The quick brown fox jumps over the lazy dog"))  
print(is_pangram("Hello World")) 

#rotate list by k positions
def rotate_list(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]
print(rotate_list([1, 2, 3, 4, 5], 2)) 

#split string into substrings show palindromic
def palindromic_splits(s):
    def is_palindrome(x):
        return x == x[::-1]
    def backtrack(start, path):
        if start == len(s):
            result.append(path)
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                backtrack(end, path + [s[start:end]])
    result = []
    backtrack(0, [])
    return result
print(palindromic_splits("aab"))

#two strings are anagram or not.py
s1, s2 = "listen", "silent"
print(sorted(s1) == sorted(s2))
