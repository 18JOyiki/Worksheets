armstrongNumberList = []


for number in range(100, 500, 1):
    t = 0
    for letter in list(str(number)):
        t += int(letter) ** 3

    if t == number:
        armstrongNumberList.append(t)


print(armstrongNumberList)
