import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"', s, re.IGNORECASE)
    if pattern:
        return "https://youtu.be/" + pattern.group(1)
    else:
        return None

if __name__ == "__main__":
    main()