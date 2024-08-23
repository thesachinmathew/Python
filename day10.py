#find the freq of each character of a string and replace each character by the aplhabet which is at distance = freq from the character
def rep(s: str) -> str:
    return ''.join(
        chr((ord(ch) - ord('a') + (s.count(ch))) % 26 + ord('a')) 
        for ch in s
    )
if __name__ == "__main__":
    print("Resulting string:", rep(input("Enter the string: ")))

#number of weekdays and date of first monday in a given month and yearimport calendar
from datetime import datetime
m, y = 8, 2024
cal = calendar.Calendar()
wee = [0] * 7
mon = None
for day, wd in cal.itermonthdays2(y, m):
    if day:
        wee[wd] += 1
        if wd == 0 and mon is None:
            mon = datetime(y, m, day)
tow = sum(wee[:5]) 
print(f"Total number of weekdays: {tow}")
print(f"Date of the first Monday: {mon.strftime('%Y-%m-%d') if mon else 'None'}")


#get string input add ^ if a character is vowels and add @ after character if not vowel 
print(''.join(c + '^' if c in 'aeiouAEIOU' else c + '@' for c in input()))

#avg students in library
en= [40, 20, 10, 30, 20]
le= [20, 10, 20, 10, 15]
def avg(en, le):
    cs = 0
    ts = 0
    for e, l in zip(en, le):
        cs += e - l
        ts += cs
    return ts / len(en)
print("Average number of students in the library:", avg(en, le))

#take 2 list as input, create a third list with appending first element of 1st and 2nd list so on , if length of the list are not the same the remaining elements append to be last
n = [1, 3, 5, 7, 8]
m = ['a', 'b', 'c', 'd', 'u', 'h', 'i']
l = min(len(n), len(m))
mer= [val for pair in zip(n[:l], m[:l]) for val in pair]
rem= n[l:] + m[l:]
print("Merged List:", mer)
print("Remaining List:", rem)
