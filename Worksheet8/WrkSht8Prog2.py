string = input("Enter a string: ")
t = 0
for letter in string:
    if letter.isnumeric():
        t += int(letter)
print(t)

    