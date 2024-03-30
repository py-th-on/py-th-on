import random
from words import words
import string
def get_valid_word(words):
    random_word = random.choice(words)
    while 'ö' in random_word or 'ä' in random_word or 'ü' in random_word or len(random_word) > 6:
        random_word = random.choice(words)
    return random_word



def hangman():
    random_word = get_valid_word(words)
    word_letters = set(random_word) #letters the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    lives = 6
    print(f'Willkommen im Hangman spiel. Erraten sie das Wort bevor ihre Lebenszahl erlischt.')
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letter used
        #' '.join(['a', 'b', 'c']) -> 'a b c'
        print(f"Du hast insgesamt {lives} leben übrig\n")
        print("Benutze Buchstaben: ", ' '.join(used_letters))
        #what current word is f.e (W _ O R D)
        word_list = [letter if letter in used_letters else '_' for letter in random_word]
        print('Das Wort ist zurzeit: ', ' '.join(word_list))
        user_letter = input("Eratten Sie einen Buchstaben: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 #takes a letter away if the user guesses a wrong letter
                print('Der Buchstabe beinhaltet nicht das Wort.\n')
        elif user_letter in used_letters:
            print("Der Buchstabe wurde schon benutzt. Versuche es mit ein anderem Buchstabe")
        else:
            print("Du hast etwas falsches getippt. Bitte versuche es noch einmal")

    #gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("Du hast kein Leben mehr und somit hast du verloren. :(")
        print(f'Das Wort lautet: {(random_word.lower()).capitalize()}')
    else:
        print(f"Du hast das Wort {random_word} richtig geraten!!")


hangman()