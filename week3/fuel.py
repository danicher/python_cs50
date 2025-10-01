def main():
    perc = frac_to_perc("Fraction: ")
    if (perc >= 99):
        print ("F")
    elif (perc <= 1):
        print("E")
    else:
        print(f"{perc}%")

def frac_to_perc(prompt):
    while True:
        try:
            frac = input(prompt)
            x, y = frac.split("/")
            x = int(x)
            y = int(y)
            if (x > y or x < 0 or y < 0):
                continue
            return round((x / y) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()