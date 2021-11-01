# 6. Write a program to calculate the electricity bill (accept number of unit from user)
# according to the following criteria :
# First 100 units - no charge
# Next 100 units - 5c per unit
# After 200 units - 10c per unit
# (For example if the units input is 350 than total bill amount is 2000 cent)

units = float(input("Enter total units of electricity: "))
bill = 0
if units > 100:
    units -= 100
    if units > 100:
        bill += 100 * 5
        print(bill)
        units -= 100
        if units > 100:
            bill += units * 10
            units -= units
    else:
        bill *= units * 5

print(f"Bill is €{bill / 100:.2f}")
