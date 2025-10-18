import pyfiglet
import random
import string
import tabulate
from termcolor import colored

def main():
    figlet = pyfiglet.Figlet()
    figlet.setFont(font="slant")
    text = figlet.renderText("Welcome to spelling bee!")
    print(colored(text, 'yellow'))

    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's start the game!")

    print("\nIn this game, you will have to create English words using the given letters")
    print("\nThe rules are simple:")
    print("1. You must use the main letter at least once in your word")
    print("2. You can only use the given letters")
    print("3. You can use the letters as many times as you want")
    print("4. Your word must be at least 4 letters long")
    print("5. You cannot use proper nouns, abbreviations, or hyphenated words")
    letters, main = generate_letters()
    display_letters(letters, main)

    while True:
        ans = input("\nDo you want new letters? (y/n): ").strip().lower()
        if ans == 'n':
            break
        elif ans == 'y':
            letters, main = generate_letters()
            display_letters(letters, main)
        else:
            print("Invalid input, please enter 'y' or 'n'", end="")

    score = 0
    words_found = []

    while True:
        try:
            word = input(f"\nEnter your word (or press 'CTRL + C' to quit): ").strip().upper()
            if not word:
                print(colored("Input cannot be empty", 'red'), end="")
            elif len(word) < 4:
                print(colored("Word must be at least 4 letters long", 'red'), end="")
            elif main not in word:
                print(colored(f"Word must contain the main letter: '{main}'", 'red'), end="")
            elif any(letter not in letters for letter in word):
                print(colored("Word contains invalid letters", 'red'), end="")
            elif (is_valid(word)):
                if word in words_found:
                    print(colored(f"You have already found the word '{word}'", 'red'), end="")
                    continue
                else:
                    words_found.append(word)
                    if (len(word) == 4):
                        points = 1
                    elif (len(word) == 5):
                        points = 5
                    elif (len(word) == 6):
                        points = 6
                    else:
                        points = 10
                    score += points
                    print(colored(f"Great! +{points} points!", 'green'))
                    print(colored(f"Your total score is: '{score}'", 'cyan'), end="")
            else:
                print(colored(f"Sorry, '{word}' is not a valid word", 'red'), end="")
        except KeyboardInterrupt:
            print(colored(f"\nYour score was: {score}", 'cyan'))
            break

    with open("finalProject/scoreboard.txt", "a") as file:
        file.write(f"{name}: {score}\n")

    print("\nScoreboard:")
    try:
        with open("finalProject/scoreboard.txt", "r") as file:
            lines = file.readlines()
            scores = []
            for line in lines:
                parts = line.strip().rsplit(": ", 1)
                if len(parts) == 2 and parts[1].isdigit():
                    scores.append((parts[0], int(parts[1])))
            scores.sort(key=lambda x: x[1], reverse=True)
            print(tabulate.tabulate(scores, headers=["Name", "Score"], tablefmt="grid"))
    except FileNotFoundError:
        print(colored("Scoreboard file not found, no scores to display", 'red'))

    text = figlet.renderText("Thanks for playing! Goodbye!")
    print(colored(text, 'yellow'))
        

def generate_letters():
    vowels = list("AEIOU")
    chosen_vowels = random.sample(vowels, 3)

    remaining_letters_pool = [c for c in string.ascii_uppercase if c not in chosen_vowels]
    chosen_others = random.sample(remaining_letters_pool, 6)

    letters = chosen_vowels + chosen_others
    random.shuffle(letters)

    main = random.choice(letters)

    return letters, main

def display_letters(letters, main):
    others = [l for l in letters if l != main]
    half = len(others) // 2
    arranged = others[:half] + [main] + others[half:]

    print("\nThe letters are: ", end="")
    for letter in arranged:
        if letter == main:
            mainLetter = colored(letter, 'yellow')
            print(f"{mainLetter}", end=" ")
        else:
            print(letter, end=" ")

def is_valid(word):
    try:
        with open("finalProject/words.txt", "r") as file:
            valid_words = set(line.strip().upper() for line in file)
        return word in valid_words
    except FileNotFoundError:
        print(colored("Word list file not found, please ensure 'words.txt' is in the correct directory", 'red'))
        return False

if __name__ == "__main__":
    main()