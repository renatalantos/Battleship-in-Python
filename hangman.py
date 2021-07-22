
import random


word_list=['haha']
bla = ['bla']
haha =['cupid']
cats=[word_list, bla, haha]
    
def display_welcome_message():
    print('Hello! Welcome! Play my hangman game!\n')
    name = input('Please enter your name: \n').upper()
    print(f'Thank you, {name}! You are ok to play!')

def choose_cat(input):
    input = input('enter cat')
    if input == 2:
        use_bla(bla)  
        


def create_random_word():

    word = random.choice(word_list) 
    return word.upper()


def play_game(word):
    game_lines = "_" * len(word)
    words_guessed = []
    letters_guessed = []
    guess_made = False
    guesses_left = 6
    print(display_hangman(guesses_left))
    

    while not guess_made and guesses_left > 0: 
        guess_letter = input('Please guess a letter: \n').upper()
        if len(guess_letter) == 1 and guess_letter.isalpha():
            if guess_letter in letters_guessed:
                print(f'You have guessed {guess_letter} already!\n')
                already_guessed = str(letters_guessed).strip('[]')
                print(f'You have guessed the following letters so far: {already_guessed}\n')  
            elif guess_letter not in word:
                print(f'Sorry, {guess_letter} is not the word!\n')
                guesses_left -= 1
                print(display_hangman(guesses_left))
                letters_guessed.append(guess_letter)
           
            else:
                print(f'Great! {guess_letter} is in the word!')
                word_as_list = list(game_lines)
                letters_guessed.append(guess_letter)
                indexes = [i for i, letter in enumerate(word) if letter == guess_letter]
                for index in indexes:
                    word_as_list[index] = guess_letter
                game_lines = "".join(word_as_list)
                if '_' not in game_lines:
                    guess_made = True
        
        else:
            if guess_letter.isalpha() is False: 
                print('You need to enter a letter. This was a different character. \n')
            elif len(guess_letter) > 1 and guess_letter.isalpha:
                print('You entered more than one letter. \n') 
        print(game_lines)
    if guess_made:
        print('Congratulations! You guessed the word!')
    else: 
        print('Oh, no! The game is over! Here comes the hangman!') 
                              
    print(game_lines)


def display_hangman(guesses_left):
    steps = [  """
        ---------
        |       |
        |       O
        |      \|/
        |      / |
        |
        |
        -------- 
               
               """,

               """
        ---------
        |       |
        |       O
        |      \|/
        |      /
        |
        |
        -------- 
               """,

               """
        ---------
        |       |
        |       O
        |      \|/
        |
        |
        |
        -------- 
               """,       
         """
        ---------
        |       |
        |       O
        |      \|
        |
        |
        |
        -------- 
               """,
               """
        ---------
        |       |
        |       O
        |       |
        |
        |
        |
        -------- 
               """,
               """             
        ---------
        |       |
        |       O
        |     
        |
        |
        --------  
             """,
             """
        ---------
        |       |
        |       
        |    
        |
        |
        -------- 
                
    """]

    return steps[guesses_left]

    
def main():
    use_bla(bla)
    display_welcome_message()
    choose_cat(input)
    word = create_random_word()
    play_game(word)
    while input('Would you like to play another game?').upper == "Y":
        display_welcome_message()
        word = create_random_word()
        play_game(word)


if __name__ == "__main__":
    main()    



