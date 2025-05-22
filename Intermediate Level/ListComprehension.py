# Create list of squares of even numbers
nums = [1, 2, 3, 4, 5, 6, 7]
squares = [x**2 for x in nums if x % 2 == 0]
print("Squares of even numbers:", squares)
