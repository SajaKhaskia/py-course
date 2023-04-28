from words_manager import WordsManager
import words as data

# print(f'Number of words: {len(data.words_5_letters)}')
# print(f'First word: {data.words_5_letters[0]}')

wm = WordsManager()
secret = wm.select_random()
print("*********")
print(f'Random word: {secret}')
print("*********")

print("Guess the Wordle in 6 tries.")
print("Each guess must be a valid 5-letter word.")
for i in range(6):
    word = input("Your guess: ")
    if word == secret:
        print("You win")
        break
    else:
        print('Try again!')
