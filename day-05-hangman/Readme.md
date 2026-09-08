# Hangman Game 🎮

A simple command-line implementation of the classic **Hangman** game built in Python as part of the **100 Days of Code - Python Bootcamp**.

## Features

- Randomly selects a word from a predefined word list.
- Displays the Hangman ASCII art for each incorrect guess.
- Tracks the player's remaining lives.
- Prevents duplicate correct guesses.
- Win/Lose conditions with appropriate messages.
- Interactive command-line gameplay.

## Project Structure

```
.
├── main.py
├── hangman_words.py
├── hangman_art.py
└── README.md
```

## How It Works

1. A random word is selected from `hangman_words.py`.
2. The player starts with **6 lives**.
3. The player guesses one letter at a time.
4. Correct guesses reveal all matching letters.
5. Incorrect guesses reduce the remaining lives.
6. The game ends when:
   - The player guesses the complete word (**Win**)
   - The player runs out of lives (**Lose**)

## Example

```
****************************6/6 LIVES LEFT****************************
Guess a letter: a

Word to guess: _ a _ _ _

****************************6/6 LIVES LEFT****************************
Guess a letter: z

You guessed z, that's not in the word. You lose a life.

****************************5/6 LIVES LEFT****************************
```

## Concepts Practiced

- Python loops (`for`, `while`)
- Conditional statements
- Lists
- Strings
- Functions from external modules
- Importing custom modules
- Random module
- Game logic
- ASCII art

## Requirements

- Python 3.x

No external libraries are required.

## Run the Project

Clone the repository:

```bash
git clone https://github.com/Maheshwaripugal/python-projects.git
```

Navigate to the project folder:

```bash
cd Day-07-Hangman
```

Run:

```bash
python main.py
```

## Future Improvements

- Validate user input.
- Prevent repeated incorrect guesses.
- Add difficulty levels.
- Allow replay without restarting the program.
- Load words from a text file.
- Add score tracking.

## Author

**Maheshwari Pugal**

GitHub: https://github.com/Maheshwaripugal