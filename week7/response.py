from validator_collection import checkers

def main():
    email = input("What's your email address? ")
    is_valid = check_email(email)
    if is_valid:
        print("Valid")
    else:
        print("Invalid")

def check_email(email):
    return checkers.is_email(email)
    
if __name__ == "__main__":
    main()