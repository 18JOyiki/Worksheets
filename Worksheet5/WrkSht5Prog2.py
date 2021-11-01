creditCardNumber = input("Enter a card number: ")


def luhnCheck(cardNumber):
    t = 0
    for n in range(len(cardNumber)):
        # n += 1 to account for string subscripting starting from 0
        n += 1
        lastDigit = int(cardNumber[len(cardNumber) - n])
        # digits in even places
        if n % 2 == 0:
            # checks if double n is a two digit number
            if len(str(2 * lastDigit)) == 2:
                # adds digits
                t += int(str(2 * lastDigit)[0]) + int(str(2 * lastDigit)[1])
            else:
                t += 2 * lastDigit
        # digits in odd places
        else:
            t += lastDigit
    if t % 10 == 0:
        return True
    return False


if luhnCheck(creditCardNumber):
    print(f"{creditCardNumber} is a valid card number")
else:
    print(f"{creditCardNumber} is an invalid card number")
