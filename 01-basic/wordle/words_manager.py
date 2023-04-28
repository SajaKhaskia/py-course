import words as data
import random


class WordsManager:
    def __init__(self):
        self.words = data.words_5_letters

    def select_random(self):
        return random.choice(self.words)

    def check_guess(self, guess):
        pass
