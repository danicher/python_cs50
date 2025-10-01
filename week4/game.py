import random

while True:
    try:
        n = int(input("Level: "))
        if (n <= 0):
            continue
        else:
            break

    except ValueError:
        pass

number = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
        if (guess <= 0):
            continue
        elif (guess < number):
            print("Too small!")
            continue
        elif (guess > number):
            print("Too large!")
            continue
        else:
            print("Just right!")
            break

    except ValueError:
        pass