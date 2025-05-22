# Check if a number is an Armstrong number
num = int(input("Enter a number: "))
order = len(str(num))
sum_arm = sum(int(digit) ** order for digit in str(num))

if num == sum_arm:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
