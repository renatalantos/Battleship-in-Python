
import random
word_list = ['hello', 'Mamma', 'joint']
def create_random_word():

    word = random.choice(word_list)
    return word.upper()


def play_game(word):
    game_lines = "_" * len(word)
    words_guessed = []
    letters_guessed = []
    guess_made = False
    guesses_left = 6

    while not guess_made and guesses_left > 0: 
        guess = input('Please guess a letter: \n').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print(f'You have guessed the guess {guess} already!\n')  
            elif guess not in word:
                print(f'{guess} is not in the word!\n')
                guesses_left -= 1
                letters_guessed.append(guess)
           
            else:
                print(f'Great! {guess} is in the word!')
                word_as_list = list(game_lines)
                letters_guessed.append(guess)
                indexes = [i for i, letter in enumerate(word) if letter == guess]
                for index in indexes:
                    word_as_list[index] = guess
                game_lines = "".join(word_as_list)
                if '_' not in game_lines:
                    guess_made = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print('You already guessed that word!\n')
            elif guess != word:
                print(f'{guess} is not the word!\n')
                guesses_left -= 1
                words_guessed.append(guess)
                guess_made = True
                game_lines = word
        else: 
            print('Not a valid guess.\n')
        print(game_lines)
    if guess_made:
        print('You guessed the word!')
    else: 
        print('sorry')                            



def main():
    word = create_random_word()
    play_game(word)

main()    



