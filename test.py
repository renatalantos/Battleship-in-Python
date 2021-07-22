# Import random package in order to be able to generate random integers
from random import randint
import math



# Generate board by taking user input for board size, allowing it to be different sizes, using a for loop
# Validate user input


global board
board = []
# global board_size


def build_board(board_size):
    """
    returns board as lists in brackets, separated by commas. 
    Number of list elements depends on validated user input.
    """ 
    return [['O' for i in range(int(board_size))] for i in range(int(board_size))]


def print_board(board):
  
    for b in board: 
        print(*b) 


def validate_board_size(board_size):
    """
    Inside the try, user input will be converted from string value to integers.
    A ValueError is raised if a string cannot be converted to an integer,
    or if the integer is outside the given range.
    """
    try:
        if int(board_size) != 4 and int(board_size) != 6 and int(board_size) != 8 and int(board_size) != 10:
            raise ValueError

    except ValueError:
        print(f'Oops, you are not able to use "{board_size}" to set your board size, please try again. \n')
        return False
    else:
        print('You are ok to play!\n')
    return True


#  Asks for user input to set the size of the board.
# The while loop will run until the user enters a valid input.


while True:
    """
    The below code was originally in a function called set_board_size(). 
    However, the variables board and board_size must be accessed throughout the 
    whole programme, and declaring them as global variables only partially worked.
    Therefore, they are used within a while loop, which also has the build_board()
    and print_board() functions inside it.
    """
    print('Choose number 4, 6, 8, 10 to set size of the board:\n')
    board_size = input('\nEnter your number here: \n')
    if validate_board_size(board_size):
        print(f'\nYour board size is {board_size} x {board_size}.\n')
        board = build_board(board_size)
        print_board(board)  #prints out board using the * symbol, which enables
        break               #list elements to be printed on a single line with spaces.


# Prints out the number of ships based on the board size. Number of ships is half of the board_size.
def set_number_of_ships():
    global number_of_ships
    number_of_ships = math.floor(int(board_size) / 2)
    print(f'\nNumber of ships is {number_of_ships}.\n')

set_number_of_ships()


def random_row(board):
    """
    Using the randint()method from the random library,
    I generate a random element in the board[] list in the board rows. 
    This will be necessary for the user guess and the
    ship placement on the board.
    Based on https://www.youtube.com/watch?v=7Ki_2gr0rsE&t=300s

    """
   
    return randint(1, len(board))


def random_col(board):
    """
    Using the randint()method from the random library,
    I generate a random element in the board[] list in the board columns. 
    This will be necessary for the user guess and the
    ship placement on the board.
    Based on https://www.youtube.com/watch?v=7Ki_2gr0rsE&t=300s

    """
    
    return randint(1, len(board))
    

random_row(board)
random_col(board)


ship_row = random_row(board)
ship_col = random_col(board)


print(f'Ship row is: {ship_row}')
print(f'Ship col is: {ship_col}')



guesses = False
# Ask user for input to guess the row
def make_guesses():

    guesses_left = int(board_size) * 4 - 5
    while guesses_left > 0 and guesses is False:
        print(f'Number of guesses left: {guesses_left}')    
        guess_row = int(input('\nEnter a number within your board size range to guess the row:\n'))
        guess_col = int(input('\nEnter a number within your board size range to guess the column:\n'))

        if ship_row == guess_row and ship_col == guess_col:
            board[guess_row-1][guess_col-1] = 'H'
            print_board(board)
            print('\nHit!\n')
            guesses_left -=1
            (f'Number of steps left: {guesses_left}')

            if board[guess_row-1][guess_col-1] == 'H':
                print('GAME OVER!')
                break

        else:
            if int(guess_row) not in range(1, int(board_size)+1) or int(guess_col) not in range(1, int(board_size)+1):
                #raise IndexError
                print('OOps, that is outside the ocean!') 
            elif board[guess_row-1][guess_col-1] == 'H' or board[guess_row-1][guess_col-1] == 'X':
                print('You have made that guess already!\n')
                if guesses_left == 1:
                    print('GAME OVER!')
                    break
            else:
                board[guess_row-1][guess_col-1] = 'X'
                print_board(board) 
                print('\nMiss!\n')
                guesses_left -=1
                (f'Number of steps left: {guesses_left}')

                if guesses_left == 1:
                    print('GAME OVER!')
                    break


make_guesses()









