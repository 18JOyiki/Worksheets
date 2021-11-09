height = int(input("Enter a height: "))
for row in range(1, height + 1):
    for block in range(0, row, 1):
        print("#", end="")
    print()
 