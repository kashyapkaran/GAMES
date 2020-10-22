import random

lives = 9

words = ['pizza', 'fairy', 'teeth', 'shirt',
'otter', 'plane','swift','stone','water','trunk']

secret_word = random.choice(words)

clue = list("?????")

heart = "❤"

guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        
        index = index + 1
        
while lives > 0:
    print(clue)
    print('Lives left: ' + heart  * lives)
    guess = input('Guess a letter or the whole word: ')
    if guess == secret_word:
        guessed_word_correctly = True
        break
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1
        
if guessed_word_correctly:
    print("you won! the secret word was "+ secret_word)
    
else:
    print("you lost! the secret word was "+ secret_word)


