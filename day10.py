#find the freq of each character of a string and replace each character by the aplhabet which is at distance = freq from the character
def rep(s: str) -> str:
    f = {}
    for ch in s:
        if ch in f:
            f[ch] += 1
        else:
            f[ch] = 1
    res = []
    for ch in s:
        freq = f[ch]
        nw = chr((ord(ch) - ord('a') + freq) % 26 + ord('a'))
        res.append(nw)
    return ''.join(res)
if __name__ == "__main__":
    inn = input("Enter the string: ")
    op = rep(inn)
    print("Resulting string:", op)
