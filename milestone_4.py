import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        Check if the guessed letter is in the word and manage 
        lives and letters left accordingly.
        '''
        letter = guess.lower()
        if letter in self.word:
            print(f'Good guess! {letter} is in the word.')
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        '''
        Ask the user to guess a letter and handle invalid input.
        '''
        while True:
            guess = input('Enter a single letter: ')
            if len(guess) != 1 and not guess.isalpha():
                print(f'Invalid letter. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
