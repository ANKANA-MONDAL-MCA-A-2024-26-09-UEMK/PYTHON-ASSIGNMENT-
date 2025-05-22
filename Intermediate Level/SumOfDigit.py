# Program to find the sum of digits (handles negative numbers too)
num = int(input("Enter a number: "))
sum_digits = 0

# Work with the absolute value of the number
temp = abs(num)

while temp > 0:
    sum_digits += temp % 10
    temp //= 10

print("Sum of digits:", sum_digits)

