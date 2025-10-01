import sys
import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    filename = sys.argv[1]

    try:
        with open(filename) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 1
    content = []

    for line in lines:
        if (count == 1):
            header = line.rstrip().split(",")
        else:
            content.append(line.split(","))

        count += 1

    print(tabulate.tabulate(content, headers=header, tablefmt="grid"))

if __name__ == "__main__":
    main()