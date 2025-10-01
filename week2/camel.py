camel_text = input("camelCase: ")
snake_text = ""
i = 0

for i in range(len(camel_text)):
    if (camel_text[i] >= "A" and camel_text[i] <= "Z"):
        snake_text = snake_text + "_" + camel_text[i].lower()
    else:
        snake_text += camel_text[i]
    i += 1

print("snake_case:", snake_text)