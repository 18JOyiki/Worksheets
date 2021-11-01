n = 0
while not n > 0:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        continue


