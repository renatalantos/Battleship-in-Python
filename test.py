# Import random package in order to be able to generate random integers
from random import randint

# Generate board, allowing it to be different sizes, using a for loop


# Validate user input
board_size = int(input('Enter number 4, 6, 8, 10 to set size of the board:\n'))
board = []

def set_board_size():
    """
    Ask for user input to set the size of the board, which will
    also determine the number of ships and the number of steps allowed for the game.
    The while loop will run until the user enters a valid input.
    """
    while True:
        print('Enter number 4, 6, 8, 10 to set size of the board:\n')
        board_size = int(input('Enter your number here:\n'))
        if validate_board_size():
            print(f'Ok, your board size is {board_size} x {board_size}')
            generate_board() 
            break
    return board_size
    


def generate_board():
    for i in range(board_size):
        board.append('O')
        print('O')


def validate_board_size():
    """
    Inside the try, user input will be converted from string value to integers.
    A ValueError is raised if a string cannot be converted to an integer,
    or if the integer is outside the given range.
    """
    try:
        if board_size != 4 and board_size !=6 and board_size !=8 and board_size != 10:
            raise ValueError(int(input('Wrong input. Please enter number 4, 6, 8, 10. \n')))
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True           

set_board_size()







