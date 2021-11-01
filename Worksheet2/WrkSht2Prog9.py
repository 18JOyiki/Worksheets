n = 0
while not 0 < n < 8:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Bad input.")
        continue

dayList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(dayList[n - 1])
