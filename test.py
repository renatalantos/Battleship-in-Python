# Import random package in order to be able to generate random integers
from random import randint
import math

# Generate board by taking user input for board size, allowing it to be different sizes, using a for loop
# Validate user input
global board = []
global board_size


def set_board_size():
    """
    Asks for user input to set the size of the board.
    The while loop will run until the user enters a valid input.
    """
    while True:
        print('Choose number 4, 6, 8, 10 to set size of the board:\n')
        global board_size
        board_size = input('\nEnter your number here: \n')
        if validate_board_size(board_size):
            print(f'\nYour board size is {board_size} x {board_size}.\n')
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


build_board(board_size)


def print_board():
    board = build_board(board_size)
    for b in board: 
        print(*b)  #  prints out board using the * symbol, which enables


print_board()



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


set_board_size()


def set_number_of_ships():
    global number_of_ships
    number_of_ships = math.floor(int(board_size) / 2)
    print(f'\nNumber of ships is {number_of_ships}.\n')


set_number_of_ships()   













