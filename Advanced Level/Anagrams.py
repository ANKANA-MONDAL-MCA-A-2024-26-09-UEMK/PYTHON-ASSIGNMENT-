from collections import defaultdict

def group_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagram_dict[key].append(word)
    return list(anagram_dict.values())

words = ["bat", "tab", "cat", "act", "tac"]
print("Grouped Anagrams:", group_anagrams(words))
