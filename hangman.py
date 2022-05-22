
import random
from dict import dict
from hangman_visual import livesVisual
import string


def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = getValidWord(dict)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()

    lives = 7

    # getting input from user
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(usedLetters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in usedLetters else '-' for letter in word]
        print(livesVisual[lives])
        print('Current word: ', ' '.join(word_list))

        userLetter = input('Guess a letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in word_letters:
                word_letters.remove(userLetter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', userLetter, 'is not in the word.')

        elif userLetter in usedLetters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(livesVisual[lives])
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


if __name__ == '**main**':
    hangman()