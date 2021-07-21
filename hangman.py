from words import word_list
import random

def create_random_word():
    
    word = random.choice(word_list)
    return word.upper()


create_random_word()

def play_game():
   # game_lines = '_' * len(word)
    #words_guessed = []
    letters_guessed = []
    guess_made = False
    guesses_left = 6

    while not guess_made and guesses_left > 0: 
        letter = input('Please enter a letter: \n').upper()
        if letter == 1 and letter.isalpha():
            if letter in letters_guessed:
                print(f'You have guessed the letter {a} already!\n')  
        elif letter not in word:
            print('You have guessed that already!')
            print(" ".join(letters_guessed))
        else:
            letters_guessed.append(letter)

play_game()            



