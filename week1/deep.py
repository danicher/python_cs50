text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
if (text != "42" and text != "forty two" and text != "forty-two"):
    print("No")
else:
    print("Yes")