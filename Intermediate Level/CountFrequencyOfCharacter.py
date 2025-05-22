# Count frequency of characters
text = input("Enter a string: ")
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print("Character frequencies:", freq)
