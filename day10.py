#find the freq of each character of a string and replace each character by the aplhabet which is at distance = freq from the character
def rep(s: str) -> str:
    return ''.join(
        chr((ord(ch) - ord('a') + (s.count(ch))) % 26 + ord('a')) 
        for ch in s
    )
if __name__ == "__main__":
    print("Resulting string:", rep(input("Enter the string: ")))

#number of weekdays and date of first monday in a given month and year
from datetime import datetime, timedelta
def a(year, month):
    fst = datetime(year, month, 1)
    fmon = fst + timedelta(days=(7 - fst.weekday()) % 7)
    wec = sum(1 for i in range(1, (fst.replace(day=28) + timedelta(days=4)).day + 1) if fst.replace(day=i).weekday() < 5)
    return wec, fmon
if __name__ == "__main__":
    year = int(input())
    month = int(input())
    we, mon = a(year, month)
    print(f"Number of weekdays: {we}\nDate of the first Monday: {mon.strftime('%Y-%m-%d')}")
#get string input replace with caps symbol if a character is vowels and add 2 after character if not vowel 
print(''.join('^' if c in 'aeiouAEIOU' else c + '@' for c in input()))
