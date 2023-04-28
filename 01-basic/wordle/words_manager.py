import words as data
import random


class WordsManager:
    def __init__(self):
        self.words = data.words_5_letters
        self.secret = self.select_random()

    def select_random(self):
        return random.choice(self.words)

    def check_guess(self, guess):
        # print(f'Number of words: {len(guess)}')
        for i in range(5):
            for letter in guess:
                if letter != self.secret[i]:
                    letter = '_'
                print(letter, end="")
                i += 1
            break

    def print_secret(self):
        print("*********")
        print(f'Random word: {self.secret}')
        print("*********")

    def print_instructions(self):
        print("How to play:")
        print("Guess the Wordle in 6 tries.")
        print("Each guess must be a valid 5-letter word.")
        # print("The color of the tiles will change to show how close your guess was to the word.")
