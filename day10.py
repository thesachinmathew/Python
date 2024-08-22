#find the freq of each character of a string and replace each character by the aplhabet which is at distance = freq from the character
def replace_by_distance(s: str) -> str:
    frequency = {}
    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    result = []
    for ch in s:
        freq = frequency[ch]
        new_char = chr((ord(ch) - ord('a') + freq) % 26 + ord('a'))
        result.append(new_char)
    return ''.join(result)
if __name__ == "__main__":
    input_string = input("Enter the string: ")
    output_string = replace_by_distance(input_string)
    print("Resulting string:", output_string)
