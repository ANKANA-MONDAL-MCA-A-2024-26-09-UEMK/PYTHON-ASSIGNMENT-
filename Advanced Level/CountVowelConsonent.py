def count_vowels_consonants(text):
    vowels = 'aeiouAEIOU'
    v = c = 0
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    print("Vowels:", v, "| Consonants:", c)

count_vowels_consonants("Python Programming")
