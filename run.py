# python code goes here# Import random package in order to be able to generate random integers
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



def validate_guess_row(guess_row):
    """
    Validates string input for row guess.
    It raises a IndexError if input given is out of range
    by validating it as an integer 
    and raises a ValueError if input is a letter or a 
    non-alphanumeric character.
    """
    
    try:
        if int(guess_row) not in range(1, int(board_size)+1):
            raise IndexError
    except IndexError:
        print('This number is out of range!\n')
        if guess_row.isalpha or guess_row.isalnum() is False:
            raise ValueError
    except ValueError:
        print(f'{guess_row} is not a number.')
        return False
    else:
        
        return True

# 
# while True:         #Until user gives valid input, the loop runs.
#     print('\nEnter a number  to guess the row:\n')
#     guess_row = input('Guess row: ')
#     if validate_guess_row(guess_row):
#         break      #The loop breaks when user enters valid input.

        

def validate_guess_col(guess_col):
    """
    Validates string input for row guess.
    It raises a IndexError if input given is out of range
    by validating it as an integer 
    and raises a ValueError if input is a letter or a 
    non-alphanumeric character.
    """
        
    try:
        if int(guess_col) not in range(1, int(board_size)+1):
            raise IndexError
    except IndexError:
        print('This number is out of range!\n')
        
        if guess_col.isalpha or guess_col.isalnum() is False:
            raise ValueError
    except ValueError:
        print(f'{guess_col} is not a number.')
        return False
 
    else:
    
        return True


#while True:   #Until user gives valid input, the loop runs
#    print('\nEnter a number  to guess the row:\n')
#    guess_col = input('Guess col: ')
#    if validate_guess_col(guess_col):
#        break    #Until user gives valid input, the loop runs


guesses = False


def make_guesses():
    """
    The while loop handles user input after validation.
    On the outside it runs on the condition that there are available guesses.
    Hits and misses are determinded by the available characters on the board,
    which will update after hits and misses.
    If user enters an invalid guess or has guessed the current intersection of
    row and column already, the available guesses won't update.
    """

    
    guesses_left = int(board_size) * 4 - 5
    while guesses_left > 0 and guesses is False:
        #print(f'Number of guesses left: {guesses_left}')
        guess_row = input('\nEnter a number within your board size range to guess the row:\n')
        try:
            if int(guess_row) not in range(1, int(board_size)+1):
                raise IndexError
        except IndexError:
            print('Oops, out of the ocean!\n')
            continue
        
            if guess_row.isalpha or guess_row.isalnum() is False:
                raise ValueError
        except ValueError:
            print(f'"{guess_row}" is not a number.')
            continue
 
        else:
            break
    
        return True
        guess_col = int(input('\nEnter a number within your board size range to guess the column:\n'))

        try:
            if int(guess_col) not in range(1, int(board_size)+1):
                raise IndexError
        except IndexError:
            print('Oops, out of the ocean!\n')
            continue
        
            if guess_col.isalpha or guess_col.isalnum() is False:
                raise ValueError
        except ValueError:
            print(f'{guess_col} is not a number.')
            continue
 
        else:
            break
    
        return True
      

        if ship_row == guess_row and ship_col == guess_col: # First condition to check is whether user
            board[guess_row-1][guess_col-1] = 'H'           # row and column correctly. If randomly-generated 
            print('\nHit!\n')                               # ship_row and user's guess_row and randomly-generated    
            guesses_left -=1                                # ship_col and guess_col are intersected, there is a hit.
            (f'Number of steps left: {guesses_left}')

            if board[guess_row-1][guess_col-1] == 'H':     # As there is only one ship, a hit is the end of the game.
                print('GAME OVER!')
                break

        else:
            
            if board[guess_row-1][guess_col-1] == 'H' or board[guess_row-1][guess_col-1] == 'X':
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




