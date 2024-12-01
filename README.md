# Number Guessing Game

This is a simple number guessing game implemented in Python. 
The program generates a random number between **0** and **1000**, and the player tries to guess it.
The game provides hints if the guess is too high or too low.

## How to Play
1. Run the script in a Python interpreter.
2. Answer whether you are "Adam" (`Y` for Yes, `N` for No`).
3. If you are Adam:
   - Guess the number by typing a number between **0** and **1000**.
   - You have **10 attempts** to guess the correct number.
   - Type `-1` to exit the game at any time.
4. If you guess correctly, you win! If you run out of attempts, you lose.

## Features
- Handles invalid inputs gracefully (e.g., non-numeric entries).
- Provides feedback on each guess (higher/lower).
- Simple and user-friendly interface.

## Requirements
- Python 3.x

## Example Run
Are you Adam? (Y/N): Y Guess a number between 0 and 1000. Type -1 to quit the game.
Please give a number to guess: 500 The number is higher than your guess! 
Please give a number to guess: 750 The number is lower than your guess!
... Congratulations! You guessed the number 732 in 6 attempts!

Enjoy the game! 🎉
