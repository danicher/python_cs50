text = input("Input: ")
new_text = ""
i = 0

for i in range(len(text)):
    char = text[i].lower()
    if (char != "a" and char != "e" and char != "i" and char != "o" and char != "u"):
        new_text += text[i]

print("Output:", new_text)