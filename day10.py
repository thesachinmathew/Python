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

#using dictionary
data = {
    1: {'entering': 40, 'leaving': 20},
    2: {'entering': 20, 'leaving': 10},
    3: {'entering': 10, 'leaving': 20},
    4: {'entering': 30, 'leaving': 10},
    5: {'entering': 20, 'leaving': 15}
}
def average_students(data):
    current_students = 0
    total_students = 0
    hours = len(data)
    
    for hour in range(1, hours + 1):
        e = data[hour]['entering']
        l = data[hour]['leaving']
        current_students += e - l
        total_students += current_students
        print(f"Hour {hour}: Entering={e}, Leaving={l}, Current Students={current_students}")
    
    return total_students / hours

print("Average number of students in the library:", average_students(data))
