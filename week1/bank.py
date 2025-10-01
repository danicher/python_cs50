def main():
    text = input("Greeting: ").strip().lower()
    sum = check_sum(text)
    print(sum)

def check_sum(str):
    if (str[0:5] == "hello"):
        return "$0"
    elif (str[0] == "h"):
        return "$20"
    else:
        return "$100"

main()