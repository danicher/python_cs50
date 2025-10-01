def main():
    text = input("Expression: ")
    x, y, z = text.split(" ")
    x = float(x)
    z = float(z)
    result = check_result(x, y, z)
    print(result)

def check_result(num1, oper, num2):
    if (oper == "+"):
        return num1 + num2
    if (oper == "-"):
        return num1 - num2
    if (oper == "*"):
        return num1 * num2
    if (oper == "/" and num2 != 0):
        return num1 / num2
    else:
        return "Error"

main()