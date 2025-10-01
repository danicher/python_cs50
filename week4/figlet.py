import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()

if (3 != len(sys.argv) != 1):
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font"):
        sys.exit("Invalid uasge")
    elif (sys.argv[2] not in font_list):
        sys.exit("Invalid uasge")

text = input("Input: ")

if len(sys.argv) == 1:
    font = random.choice(font_list)
    figlet.setFont(font=font)
else:
     font = sys.argv[2]
     figlet.setFont(font=font)

output = figlet.renderText(text)
print(output)