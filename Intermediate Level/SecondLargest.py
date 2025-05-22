# Find the second largest number
lst = [10, 20, 4, 45, 99]
lst = list(set(lst))  # Remove duplicates
lst.sort()
print("Second largest number:", lst[-2])
