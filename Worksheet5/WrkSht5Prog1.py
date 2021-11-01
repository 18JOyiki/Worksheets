import math
import random

A = int(input("Enter a number: "))
B = int(input("Enter another: "))

lower = A if A < B else B
upper = B if B > A else A


randomChoice = random.randint(lower, upper)

guess = None
usrGuessCount = 0
minGuessCount = round(math.log(upper - lower + 1, 2))
while guess != randomChoice:
    guess = int(input("Take a guess: "))
    usrGuessCount += 1
    if guess > randomChoice:
        print("Too high")
    elif guess < randomChoice:
        print("Too low")
    elif minGuessCount == 0 and usrGuessCount == 1:
        usrGuessCount -= 1


result = usrGuessCount <= minGuessCount

if result:
    print("Congratulations you win!")
else:
    print(f"You were {usrGuessCount - minGuessCount} off. Better luck next time!")






