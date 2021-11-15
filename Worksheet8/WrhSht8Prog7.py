kebab = input("Enter a word in kebab-case: ")
for char in kebab:
    if char == "-":
        print()
    else:
        print(char, end="")
