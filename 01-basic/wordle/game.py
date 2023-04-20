from words_manager import WordsManager
import words as data

print(f'number of words: {len(data.words_5_letters)}')
print(f'first word: {data.words_5_letters[0]}')

wm = WordsManager()
print(f'random word: {wm.select_random()}')