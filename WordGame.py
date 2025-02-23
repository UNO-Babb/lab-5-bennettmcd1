#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter in word

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    return word[spot] == letter

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    
    feedback = ""
    
    # First, we need to check each letter in the guess
    for i in range(len(myGuess)):
        if inSpot(myGuess[i], word, i):  # If the letter is in the right spot
            feedback += myGuess[i].upper()  # Capitalize it
        elif inWord(myGuess[i], word):  # If the letter is in the word but in the wrong spot
            feedback += myGuess[i].lower()  # Make it lowercase
        else:  # If the letter is not in the word at all
            feedback += "*"

    return feedback

def main():
    # Pick a random word from the list of all words
    with open("words.txt", 'r') as wordFile:  # Using 'with' ensures the file is properly closed
        content = wordFile.read()
        wordList = content.split("\n")
    
    # Clean up the word list to remove any empty lines and select a random word
    wordList = [word.strip() for word in wordList if word.strip()]
    todayWord = random.choice(wordList)

    # Inform the user (remove this in the actual game to prevent cheating)
    print(f"Debug: The word is '{todayWord}'")  # This is for testing, remove or comment out in the final version
    
    # User has 6 guesses to figure out the word
    attempts = 6
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        myGuess = input("Enter your guess (5-letter word): ").strip().upper()  # Ensure upper case

        # Check if the word is 5 letters long
        if len(myGuess) != 5:
            print("Please enter a 5-letter word.")
            continue
        
        if myGuess == todayWord:
            print("Congratulations! You've guessed the word correctly!")
            break
        
        # Get the feedback on the guess
        feedback = rateGuess(myGuess, todayWord)
        print("Feedback:", feedback)
        
        attempts -= 1  # Reduce the number of attempts left

    # If out of attempts, tell the user the correct word
    if attempts == 0:
        print(f"Sorry, you've run out of attempts! The correct word was '{todayWord}'.")

if __name__ == '__main__':
    main()