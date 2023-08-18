# Program written by ailam_7
# If you find anything wrong, let me know at info@mohamedailam.com

import re
from random import randrange

# The ASCII art used in the program is taken from
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c


# Return the length of the word as a list filled with underscores
def encapsulate_word(word):
    underscores = []
    for x in word:
        underscores.append("_")
    return underscores

# Prints the dashed line that separates each turn
def print_dashed_line():
    print("")
    dashedLine = ["/"] * 20
    print(*dashedLine)
    print("")


# Main method of program
def main():
    # Read in the Ascii art of the Noose from the ascii art.txt file
    with open("ascii_art.txt", "r") as file:
        stages = file.read().split("\n")

    # Read in the words from the catalogue of words in words.txt
    with open('words.txt', 'r') as file:
        words_dict = {}
        for line in file:
            line = line.strip()
            word, hint = line.split(',')
            words_dict[word] = hint

    # Randomly select a word from the catalogue
    random1 = randrange(len(words_dict))  # For the category
    word = list(words_dict)[random1]
    word = word.upper()
    hint = list(words_dict.values())[random1].upper()
    print(f"\nThe word to be guessed has {len(word)} letters!")
    print(f"Hint: {hint}")

    hiddenWord = encapsulate_word(word)
    guesses = 7
    gameWon = False


    # While loop that runs during the game
    while guesses != 0:
        print_dashed_line()
        print(f"You have {guesses} guesses left!")
        print(f"Hint: {hint}")
        print(*hiddenWord)
        # Prints the ascii art according to guesses left
        for stage in stages[(7 - guesses) * 7 : (8 - guesses) * 7]:
            print(stage)
        guess = input("Enter your guess: ")
        guess = guess.upper()

        # First and foremost check if guess contains alphabets only
        if guess.isalpha():
            #  Execute if guess is only a letter
            if len(guess) == 1:
                if guess in word:
                    if word.count(guess) == 1:
                        position = word.index(guess)
                        hiddenWord[position] = guess
                        print("Correct guess!")
                    elif word.count(guess) > 1:
                        indexes = [
                            match.start() for match in re.finditer(guess, word)
                        ]
                        for index in indexes:
                            hiddenWord[index] = guess
                    # Quick check if all the letters in the word have been guessed
                    if not "_" in hiddenWord:
                        gameWon = True
                        break
                else:
                    print("Sorry, that letter is not in the word!")
                    guesses = guesses - 1

            # If user tries to directly guess the word
            if len(guess) > 1:
                if word == guess:
                    gameWon = True
                    break
                else:
                    print("Sorry!, that is not the correct word!")
                    guesses = guesses - 1
        else:
            print("Guess cannot contain non-alphabetical characters!")


    # Game ending states
    print_dashed_line()
    if gameWon:
        print("Congratulations! You guessed the correct word")
        print(f"The word was: {word}")
    else:
        print("Uh oh! Looks like you ran out of guesses")
        print(f"The correct word was {word}!")
        print("Better luck next time")


main()
