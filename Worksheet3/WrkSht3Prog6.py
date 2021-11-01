decimal = int(input())
binary = ""
while decimal != 0:
    binary += f"{decimal % 2}"
    decimal //= 2
    
print(binary[::-1])
