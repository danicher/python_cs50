import re

def main():
    print(count(input("Text: ")))

def count(s):
    s = s.lower()
    um_count = len(re.findall(r"\bum\b", s))
    return um_count

if __name__ == "__main__":
    main()