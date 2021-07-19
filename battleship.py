# Import random package in order to be able to generate random integers
from random import randint

# Generate board by taking user input for board size, allowing it to be different sizes, using a for loop
# Validate user input
board = []


def set_board_size():
    """
    Asks for user input to set the size of the board.
    The while loop will run until the user enters a valid input.
    """
    while True:
        print('Choose number 4, 6, 8, 10 to set size of the board:\n')

        board_size = input('Enter your number here: \n')
        number_of_ships = int(board_size)-3 
        if validate_board_size(board_size):
            print(f'Your board size is {board_size} x {board_size}.\n')
            print(f'Number of ships is {number_of_ships}')
            board = build_board(board_size)
            for b in board: 
                print(*b)  #  prints out board using the * symbol, which enables
            break          #  list elements to be printed on a single line with spaces.


    return board_size


def build_board(board_size):
    """
    returns board as lists in brackets, separated by commas. 
    Number of list elements depends on validated user input.
    """ 
    return [['O' for i in range(int(board_size))] for i in range(int(board_size))]  
  

def validate_board_size(board_size):
    """
    Inside the try, user input will be converted from string value to integers.
    A ValueError is raised if a string cannot be converted to an integer,
    or if the integer is outside the given range.
    """
    try:
        if  int(board_size) != 4 and int(board_size) != 6 and int(board_size) != 8 and int(board_size) != 10:
            raise ValueError
       
    except ValueError:
        print(f'Oops, you are not able to use {board_size} to set your board size, please try again. \n')
        return False
    else:
	    print('You are ok to play!\n')
    return True  


set_board_size()


******************
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

ship_row = random_row(board) #places ship row on the board
ship_col = random_col(board) #places ship column on the board

# Ask user for input to guess the row

print(f'Ship row: {ship_row}\n')
print(f'Ship column: {ship_col}\n')


def make_guesses():

    for i in range(int(board_size) * 4 - 5, 0, -1):
        print(f'Number of guesses left: {i}')    
        guess_row = int(input('\nEnter a number within your board size range to guess the row:\n'))
        guess_col = int(input('\nEnter a number within your board size range to guess the column:\n'))

        if ship_row == guess_row and ship_col == guess_col:
            board[guess_row-1][guess_col-1] = 'H'
            print_board(board)
            print('\nHit!\n')
            #print(f'Number of steps left: {i}')

            if board[guess_row-1][guess_col-1] == 'H':
                print('GAME OVER!')
                break

        elif board[guess_row-1][guess_col-1] == 'H' or board[guess_row-1][guess_col-1] == 'X':
            print('You have made that guess already!\n')
            if i == 1:
                print('GAME OVER!')
                break


        else:
            board[guess_row-1][guess_col-1] = 'X'
            print_board(board) 
            print('\nMiss!\n')
           # print(f'Number of steps: {i}')

            if i == 1:
                print('GAME OVER!')
                break


make_guesses()

try:
            if guess_row not in range(1, int(board_size)+1) or guess_col not in range(1, int(board_size)+1):
                raise IndexError
                print('OOps, that is outside the ocean!')
            elif type(guess_row) == int is False or type(guess_col) == int is False:
                raise ValueError('Hello')

        except ValueError: 
            print('baaa')

            return False
        return True 

        **********


        def validate_guess_row(guess_row):
    try:
        if guess_row not in range(1, int(board_size)+1):
            raise IndexError
            print('OOps, that is outside the ocean')
        elif type(guess_row)== int is False:
            raise ValueError
            print('Please enter a number')
    except ValueError:        
        return False
    else:
        print('OK')    

    return True    


def validate_guess_col(guess_col):
    try:
        if guess_column not in range(1, int(board_size)+1):
            raise IndexError
            print('OOps, that is outside the ocean')
        elif type(guess_col) == int is False:
            raise ValueError
            print('Please enter a number')
    except ValueError:        
        return False
    else:
        print('OK')    

    return True


while True:
    guess_row = int(input('\nEnter a number within your board size range to guess the row:\n'))
    if validate_guess_row(guess_row):
        break

while True:
    guess_column = int(input('\nEnter a number within your board size range to guess the column:\n'))
    if validate_guess_col(guess_col):
        break







