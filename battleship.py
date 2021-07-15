# Import random package in order to be able to generate random integers
from random import randint

# Generate board, allowing it to be different sizes, using a for loop

board = []

board_size = int(input('Enter number 4, 6, 8, 10 to set size of the board:\n'))
BOARD_SIZE_FACTOR = board_size / 2  #needed a constant in order to be able to create a while loop
# Validate user input
while BOARD_SIZE_FACTOR < 2 or BOARD_SIZE_FACTOR > 5 or board_size % 2 != 0: 
    raise ValueError('Please enter number 4, 6, 8 or 10. \n')
    
if BOARD_SIZE_FACTOR == 2:
    number_of_ships = 1
elif BOARD_SIZE_FACTOR == 3:
    number_of_ships = 3
elif BOARD_SIZE_FACTOR == 4:
    number_of_ships = 4
else:
    number_of_ships = 5


print(f'Number of ships: {number_of_ships}\n')

for board_elements in range(board_size):
    board.append('O')

    print('O')



 
