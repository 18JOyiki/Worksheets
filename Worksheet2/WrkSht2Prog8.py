lastDigit = int(input("Enter a Number: ")) % 10
if lastDigit % 3 == 0:
    print("The last digit of number is divisible by 3")
else:
    print("The last digit of number is not divisible by 3")
