import random

def main():
    lvl = get_level()

    i = 0
    score = 0
    while (i < 10):
        i += 1
        n1 = generate_integer(lvl)
        n2 = generate_integer(lvl)
        attempts = 0
        while (attempts < 3):
            try:
                ans = int(input(f"{n1} + {n2} = "))
                if (ans == (n1 + n2)):
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1

            except ValueError:
                print("EEE")
                attempts += 1

        if (attempts == 3):
            print(f"{n1} + {n2} = {n1 + n2}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if (n <= 0 or n >= 4):
                continue
            else:
                return n

        except ValueError:
            pass

def generate_integer(level):
    if (level == 1):
        return random.randint(0, 9)
    elif (level == 2):
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()