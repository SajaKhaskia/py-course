from words_manager import WordsManager


# print(f'Number of words: {len(data.words_5_letters)}')
# print(f'First word: {data.words_5_letters[0]}')

wm = WordsManager()
wm.print_secret()
wm.print_instructions()

print("Let's start")
for i in range(6):
    guess = input("Your guess: ").lower()
    if len(guess) == 5:
        if guess == wm.secret:
            print("You win!")
            break
        else:
            wm.check_guess(guess)
            print("\n")
    else:
        print("Each guess must be a valid 5-letter word!")
print("Thank you for playing")

