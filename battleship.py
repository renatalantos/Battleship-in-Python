# Import random package in order to be able to generate random integers
from random import randint

# Generate board, allowing it to be different sizes, using a for loop

board = []

board_size = int(input('Enter number 4, 6, 8, 10 to set size of the board:\n'))
if board_size == 2*2:
    number_of_ships = 1
elif board_size == 2*3:
    number_of_ships = 3
elif board_size == 2*4:
    number_of_ships = 4
else: 
    number_of_ships = 5

print(f'Number of ships: {number_of_ships}\n')

for board_elements in range(board_size):
    board.append('O')

    print('O')



 
