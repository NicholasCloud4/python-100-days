import random

word_list = ["python", "hangman", "computer", "keyboard", "program", "variable", "function", "network"]

stages = [
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
guessed = []
lives = len(stages) - 1

print("Welcome to Hangman!")
print(" ".join(display))

while lives > 0 and "_" in display:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print(f"You already guessed '{guess}'.")
        continue

    guessed.append(guess)

    if guess in chosen_word:
        for position, letter in enumerate(chosen_word):
            if letter == guess:
                display[position] = letter
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

    print(stages[lives])
    print(" ".join(display))
    print(f"Lives left: {lives} | Guessed: {', '.join(guessed)}")

if "_" not in display:
    print("\nYou win!")
else:
    print(f"\nYou lose! The word was '{chosen_word}'.")
