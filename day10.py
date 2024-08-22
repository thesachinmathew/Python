#find the freq of each character of a string and replace each character by the aplhabet which is at distance = freq from the character
def rep(s: str) -> str:
    return ''.join(
        chr((ord(ch) - ord('a') + (s.count(ch))) % 26 + ord('a')) 
        for ch in s
    )
if __name__ == "__main__":
    print("Resulting string:", rep(input("Enter the string: ")))
