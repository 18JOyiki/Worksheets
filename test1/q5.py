file1 = open("readme.txt", "r")
c = 0
vowels = ["a", "e", "i", "o", "u"]
for line in file1.readline():
    for char in line.strip():
        if char.lower() in vowels:
            c += 1
print(f"there are {c} vowels in readme.txt")