import random
# Import the word lists from our category modules.
import animals, fruits, colors

# Dictionary mapping category names (as shown to the user) to the module containing the words.
category_modules = {
    "Animals": animals,
    "Fruits": fruits,
    "Colors": colors
}

# ASCII art for hangman at various stages.
hangman_drawings = [
    """
     +---+
     |   |
         |
         |
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
    /|   |
         |
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
    / \\  |
         |
    =========
    """
]

def choose_category():
    """Prompt the user to choose a category and return the corresponding module."""
    print("Available Categories:")
    categories = list(category_modules.keys())
    for idx, cat in enumerate(categories, start=1):
        print(f"{idx}. {cat}")
    
    while True:
        try:
            selection = int(input("Please choose a category by entering its number: "))
            if 1 <= selection <= len(categories):
                chosen_category = categories[selection - 1]
                print(f"\nYou selected: {chosen_category}\n")
                return category_modules[chosen_category]
            else:
                print("Invalid selection. Please choose a valid number from the list.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

def choose_word(word_list):
    """Randomly select a word from the provided list."""
    return random.choice(word_list)

def show_game_state(mistakes, guessed, secret):
    """Display the current hangman drawing, the progress on the secret word, and guessed letters."""
    print(hangman_drawings[mistakes])
    
    # Build the display string with underscores for unguessed letters.
    display_word = ""
    for ch in secret:
        if ch in guessed:
            display_word += ch + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    print("Guessed letters:", " ".join(sorted(guessed)))
    print()

def play_game():
    # Let the user choose a category.
    category_module = choose_category()
    
    # Get the word list from the chosen category.
    word_list = category_module.words
    secret_word = choose_word(word_list)
    
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(hangman_drawings) - 1

    print("Welcome to Hangman!")
    
    # Main game loop.
    while mistakes < max_mistakes:
        show_game_state(mistakes, guessed_letters, secret_word)
        guess = input("Guess a letter: ").lower().strip()

        # Validate that the input is a single alphabetical character.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.\n")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            print("That letter is not in the word.\n")
            mistakes += 1

        # Check if the player has guessed all letters in the word.
        if all(letter in guessed_letters for letter in secret_word):
            show_game_state(mistakes, guessed_letters, secret_word)
            print("Congratulations! You guessed the word correctly!")
            break
    else:
        show_game_state(mistakes, guessed_letters, secret_word)
        print("Game over! The word was:", secret_word)

if __name__ == "__main__":
    play_game()
