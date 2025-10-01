def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (len(s) >= 2 and len(s) <= 6):
        return False

    if not (is_letter(s[0]) and is_letter(s[1])):
        return False

    i = 2
    num_count = 0

    for i in range(len(s)):
        if not (is_letter(s[i]) or is_number(s[i])):
            return False

        if (is_letter(s[i]) and num_count != 0):
            return False

        if (is_number(s[i])):
            if (s[i] == "0" and num_count == 0):
                return False
            num_count +=1

    return True

def is_letter(ch):
    return ((ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z"))

def is_number(ch):
    return (ch >= "0" and ch <= "9")

main()