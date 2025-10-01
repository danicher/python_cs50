names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        print("")
        break

print("Adieu, adieu, to", end=" ")

if (len(names) == 1):
    print(names[0])
elif (len(names) == 2):
    print(names[0], "and", names[1])
else:
    i = 0
    while (i < len(names) - 1):
        print(names[i] + ", ", end="")
        i += 1

    print("and", names[i])