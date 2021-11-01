a = int(input())
b = int(input())
c = a
R = None

if a > b:
    while R != 0:
        R = a % b
        a = b
        b = R
        if R == 0:
            print(a)
           
else:
    while R != 0:
        R = b % a
        b = a
        a = R
        if R == 0:
            print(b)
