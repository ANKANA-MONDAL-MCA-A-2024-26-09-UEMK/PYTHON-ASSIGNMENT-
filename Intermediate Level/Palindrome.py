# Check if a list is palindrome
lst = [1, 2, 3, 2, 1]
if lst == lst[::-1]:
    print("List is a palindrome")
else:
    print("List is not a palindrome")
