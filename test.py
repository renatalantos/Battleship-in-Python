# Import random package in order to be able to generate random integers
from random import randint

# Generate board, allowing it to be different sizes, using a for loop


# Validate user input
board_size = int(input('Enter number 4, 6, 8, 10 to set size of the board:\n'))
board = []


def generate_board():
    for i in range(board_size):
        board.append('O')
        print('O')


def set_board_size():
    """
    Ask for user input to set the size of the board, which will
    also determine the number of ships and the number of steps allowed for the game.
    The while loop will run until the user enters a valid input.
    """
    
    if board_size != 4 and board_size !=6 and board_size !=8 and board_size != 10:
        int(input('Wrong input. Please enter number 4, 6, 8, 10. \n'))
        if board_size == 4: 
            number_of_ships = 1
            print(f'Number of ships in game: {number_of_ships}\n')
        elif board_size == 6:
            number_of_ships = 3
            print(f'Number of ships in game: {number_of_ships}\n')
        elif board_size == 8:
            number_of_ships = 4
            print(f'Number of ships in game: {number_of_ships}\n')
        elif board_size == 10:
            number_of_ships = 5
            print(f'Number of ships in game: {number_of_ships}\n') 
        generate_board()        
    
#print(f'Number of ships in game: {number_of_ships}\n')


set_board_size()







