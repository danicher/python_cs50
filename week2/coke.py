amount = 50

while (amount > 0):
    print("Amount due:", amount)
    num = int(input("Insert coin: "))

    if (num == 5 or num == 10 or num == 25):
        amount -= num

print("Change owed:", amount * -1)