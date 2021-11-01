date = input("Enter a date in the form dd/mm/YYYY: ")

dd = int(date[0:2])
mm = int(date[3:5])
year = int(date[6:10])

if mm < 3:
    mm += 12
    year -= 1

c = int(str(year)[0:2])
y = int(str(year)[2:4])

w = (dd + ((13 * (mm + 1)) // 5) + y + (y // 4) + (c // 4) - 2 * c) % 7

weekdays = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]

print(f"{weekdays[w]}")








