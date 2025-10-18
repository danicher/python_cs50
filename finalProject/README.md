# Spelling Bee
#### Video Demo: https://youtu.be/O2pJ4OUGfAE?si=D2r52HGcXUrEnCvx
#### Description:
Spelling Bee is a terminal-based Python game inspired by the New York Times puzzle of the same name. The player is given a set of 9 randomly generated uppercase letters, one of which is chosen as the **main letter**. The objective is to form as many valid English words as possible that meet the following criteria:

1. The word must be at least 4 letters long.
2. The word must include the main letter.
3. The word can only use the given 9 letters (repeating is allowed).
4. The word must be a valid English word, based on a dictionary loaded from a local file.
5. Duplicate entries are not allowed.
6. The game rejects abbreviations, proper nouns, and hyphenated words.

Words are validated against a word list (`words.txt`) and points are awarded based on length:
- 4 letters = 1 point
- 5 letters = 5 points
- 6 letters = 6 points
- 7 or more = 10 points

The game includes colored terminal output using `termcolor`, and a stylized welcome/goodbye screen using `pyfiglet`. A scoreboard is stored in `scoreboard.txt`, and previous player scores are displayed in a ranked table at the end using `tabulate`.

### Files

- `project.py`: Main game logic and word checking.
- `test_project.py`: Basic test cases using `pytest`.
- `words.txt`: A wordlist dictionary for validating words.
- `scoreboard.txt`: Saves names and scores for the leaderboard.
- `requirements.txt`: Lists required Python libraries.
- `README.md`: This file.

### Concepts Practiced

- File I/O
- Lists, sets, and strings
- User input validation
- External libraries
- Randomization
- Testing with `pytest`
- Code organization
- Terminal UI formatting

---

## How to Run

```bash
pip install -r requirements.txt
python project.py
