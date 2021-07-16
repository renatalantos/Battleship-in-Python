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
















