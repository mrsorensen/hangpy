#!/usr/bin/python

import random
import os
from os.path import expanduser

# Path to word file
pathToWords = '~/hangpy/words.txt'

# Prints a gallow with the man hanging depending on how many lives you got left
def gallow(lives):
    if lives == 6:
        print(',============')
        print('||')
        print('||')
        print('||')
        print('||')
        print('||')
        print('||')
        print('||')
        print('/ \\')
        print()
    elif lives == 5:
        print(',============')
        print('||          |')
        print('||          |')
        print('||          O')
        print('||')
        print('||')
        print('||')
        print('||')
        print('||')
        print('/ \\')
        print()
    elif lives == 4:
        print(',============')
        print('||          |')
        print('||          |')
        print('||          O')
        print('||          |')
        print('||')
        print('||')
        print('||')
        print('||')
        print('/ \\')
        print()
    elif lives == 3:
        print(',============')
        print('||          |')
        print('||          |')
        print('||          O')
        print('||         /|')
        print('||')
        print('||')
        print('||')
        print('||')
        print('/ \\')
        print()
    elif lives == 2:
        print(',============')
        print('||          |')
        print('||          |')
        print('||          O')
        print('||         /|\\')
        print('||')
        print('||')
        print('||')
        print('||')
        print('/ \\')
        print()
    elif lives == 1:
        print(',============')
        print('||          |')
        print('||          |')
        print('||          O')
        print('||         /|\\')
        print('||         /')
        print('||')
        print('||')
        print('||')
        print('/ \\')
        print()
    elif lives == 0:
        print(',============')
        print('||          |')
        print('||          |')
        print('||          O')
        print('||         /|\\')
        print('||         / \\')
        print('||')
        print('||')
        print('||')
        print('/ \\')
        print()

# Prints the revealed letters of the word. Ex: _a__rt__
def progress(secretWord, guesses):
    pos = 0
    publicWord = "_" * len(secretWord)
    publicWord = list(publicWord)
    for l in secretWord:
        if l in guesses:
            publicWord[pos] = l
        pos = pos+1
    print("".join(publicWord))
    print()

    if '_' not in publicWord:
        print('You won!')
        quit()

# Prints letters already guessed
def guessed(guesses):
    print('You\'ve guessed:', list(guesses))

# Clears the screen
def clear():
    os.system('clear')

# Adds users guessed letter to the array of guesses if it's not already there
def submitGuess(userInput, guesses):
    if userInput not in guesses:
        guesses.append(userInput)
        return True
    else:
        return False

# Open and read file with words and pick a random word
wordFile = open(expanduser(pathToWords))
wordList = wordFile.read().split('\n')
wordFile.close()
secretWord = random.choice(wordList).lower()

# Amount of lives you start with
lives = 6
# Declares user guesses as an array/list
guesses = []

# Prepares an empty error message
error = ''

# Game starts ------------

# Clear screen
clear()
# Print gallow
gallow(lives)
# Prints the revealed letters in the word
progress(secretWord, guesses)
# Prints the empty error message for formatting
print(error)
# Prints guessed letters
guessed(guesses)

# Loop
while True:
    # Lose if lives reach 0
    if lives == 0:
        clear()
        gallow(lives)
        print('You lost')
        quit()
    # Get users guessed letter or full word
    userInput = input('Guess: ')
    # Check if user guessed the right word
    if userInput == secretWord:
        print('WIN')
        quit()
    # Checks if user guessed the wrong word
    elif len(userInput) == len(secretWord):
        error = 'Wrong guess'
        lives = lives-1
    # Prevent empty guess
    elif userInput == '':
        error = 'Empty submission'
    # Prevents multiple characters in guess (unless the guessed word has as many letters as the secret word)
    elif len(userInput) != 1:
        error = 'Only one character at a time'
    else:
        # Removes life if wrong guess
        if submitGuess(userInput, guesses):
            lives = lives-1
        # Sets error if user already tried that letter
        else:
            error = 'Already tried \"{}\"'.format(userInput)
    # Clears screen
    clear()
    # Prints gallow
    gallow(lives)
    # Prints the revealed letters in the word
    progress(secretWord, guesses)
    # Prints error message (may be empty)
    print(error)
    # Prints guessed letters
    guessed(guesses)
