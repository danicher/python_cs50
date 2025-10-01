def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    name = input("")
    new_name = convert(name)
    print(new_name)

main()