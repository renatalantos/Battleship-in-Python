from random import randint


"""
Import randint package in order to be able to
generate random integers for ship rows and columns
"""
import math

"""
Import math package to be able to floor integer generated
to set ship size.
"""


"""
Generate board by taking user input for board size,
allowing it to be different sizes, using a for loop
Validate user input
"""

global board
board = []
global ships_to_hit
ships_to_hit = []
global number_of_ships


def print_graphics():

    print('____   ___  ______ ______ __     ____  __  __  __ __  __')
    print('|| )) // \\ | || | | || | ||    ||    (( \ ||  || || || \\')
    print('||=)  ||=||   ||     ||   ||    ||==   \\  ||==|| || ||_//')
    print('||_)) || ||   ||     ||   ||__| ||___ \_)) ||  || || ||')


print_graphics()


def print_end():

    print('  ___  ___  ___  ___  ____      ___   __ __  ____ ____')
    print('// \\ // \\ ||\\//|| ||        // \\  || || ||    || \\')
    print('((___ ||=|| || \/ || ||==     ((   )) \\ // ||==  ||_//')
    print('\\_|| || || ||    || ||___     \\_//   \V/  ||___ || \\')


def print_welcome():
    print("\n~~~~~~~~~~~ LET'S PLAY BATTLESHIP! ~~~~~~~~~~~\n")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print('* Welcome. I hope you will enjoy this basic battleship game.')
    print('* Please take a second to read what you need to know to play.')
    print('* Ship sizes are 1 x 1. However, ships can be next to one another.')
    print('* Ships can be duplicate. So, if all your ships are sunken and you')
    print('* do not get the message "You sank my battleships", you need to')
    print('* target one of your sunken ships again.')
    print('* You can set the size of the board.')
    print("* You'll see the number of ships remaining.")
    print("* You'll see the number of guesses remaining after the first shot.")
    print('* If you miss, the missed shot displays as an X on the board.')
    print('* If you hit, the sunken ship displays as an H on the board.')
    print('* When you ran out of guesses and there are still ships on the')
    print('* board, you lose and the game ends.')
    print('* When you sank all the ships, you win and the game is over.')
    print('* Click on the red Run Program button to restart the game.')


print_welcome()


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


def create_targets(number_of_ships):
    """
    Creates targets in number of ships by running
    through a for loop. Targets are intersections of rows and columns.
    Row and column pairs are then appended to the ships_to_hit list
    as list elements.
    """
    for hits in range(number_of_ships):
        row = random_row(board)
        col = random_col(board)
        ships_to_hit.append([row, col])


def build_board(board_size):
    """
    Returns board as lists in brackets, separated by commas.
    Number of list elements depends on validated user input.
    """
    return [['O' for i in range(int(board_size))]
            for i in range(int(board_size))]


def print_board(board):
    """
    prints the board
    """
    for b in board:
        print(*b)


def to_calculate_hits(board):
    """
    Calculates the targets in the range of the ship
    number size.
    """
    number_of_ships = math.floor(int(board_size) / 2)
    create_targets(int(number_of_ships))
    print(f'Number of ships is {number_of_ships}.')


def validate_board_size(board_size):
    """
    Inside the try, user input will be converted from string value to integers.
    A ValueError is raised if a string cannot be converted to an integer,
    or if the integer is outside the given range. This information is then fed
    back to the user.
    """
    try:
        if int(board_size) != 4 and int(board_size) != 6 \
                                and int(board_size) != 8 \
                                and int(board_size) != 10:
            raise ValueError

    except ValueError:
        print(f'Oops, you are not able to use "{board_size}"\
              to set your board size, please try again. \n')
        return False
    else:
        print('You are ok to play!\n')
    return True


while True:
    """
    The below code was originally in a function called set_board_size().
    However, the variables board and board_size must be accessed throughout the
    whole programme, and declaring them as global variables only partially
    worked.
    Therefore, they are used within a while loop, which also has the
    build_board() and print_board() functions inside it to set the size of
    the board.
    Here user is asked  for user input.
    The while loop will run until the user enters a valid input.
    """
    print('Choose number 4, 6, 8, 10 to set size of the board:\n')
    board_size = input('\nEnter your number here: \n')
    if validate_board_size(board_size):
        print(f'\nYour board size is {board_size} x {board_size}.\n')
        board = build_board(board_size)
        to_calculate_hits(board)
        print_board(board)  # * enables list elements to be printed on a
        break               # single line with spaces.

random_row(board)
random_col(board)

guesses = False
global guesses_left


def make_guesses():
    """
    The while loop handles user input after validation.
    On the outside it runs on the condition that there are available guesses.
    Hits and misses are determinded by the available characters on the board,
    which will update after hits and misses.
    If user enters an invalid guess or has guessed the current intersection of
    row and column already, available guesses won't update.
    """

    guesses_left = int(board_size) * 4 - 5
    while int(board_size) * 4 - 5 > 0 and guesses is False:
        """
        Validation to check for invalid user input.
        IndexError is raised and excepted if user enters a number outside
        of the requested range and ValueError is raised and excepted if user
        enters anything but a number.
        """

        guess_row = input(f'\nGuess row in range of 1 and {board_size}:\n')
        guess_col = input(f'\nGuess column in range of 1 and {board_size}:\n')
        print(f'\nNumber of guesses left: {guesses_left}\n')

        try:
            if int(guess_row) \
                    not in range(1, int(board_size)+1) \
                    or int(guess_col) not in range(1, int(board_size)+1):
                raise IndexError
        except IndexError:
            print('Oops, ship is out of the ocean!\n')
            continue
        except ValueError:
            print(f'\n"{guess_row}" or "{guess_col}" is not a number.\n')
            print('\nPlease check and try again!\n')
            continue
        else:
            pass
        """
        First condition is to check is whether user guessed
        row and column correctly.
        The for loop in the first if checks is guessed row and guessed
        column are indexes of the ships_to_hit list.
        If randomly-generated ship_row and user's guess_row
        are intersected, there is a hit. This is checked by
        the row and col serving as indexes in the board[] list.
        Message is displayed.
        """
        """
        The else statement and its conditions
        check for outcomes if user doesn't hit.
        """
        """
        Second condition in else is to check is what happens if user
        made a guess already. Message is displayed.
        Number of guesses are not incremented.
        """
        """
        Else in else is to check is what happens if user
        doesn't guess correctly. If intersected guessed rows and columns
        (their numbers serve as indices in board list)
        hit an X on the board, there is a miss.
        Number of guesses are incremented with each
        incorrect guess. Message is displayed.
        If number of guesses is one, user loses.
        """

        guess_correct = False  # False is default
        for hit_ship in ships_to_hit:
            """ 
            For loop iterates through the ships_to_hit list and
            checks if index 0 in ships_to hit is equal to guessed row
            and index [1] in ships_to_hit equal to guess row. If so, we have
            a hit. Updated board is printed. This is necessary as we have more
            than one ship.
            """
            if hit_ship[0] == int(guess_row) and hit_ship[1] == int(guess_col):
                board[int(guess_row)-1][int(guess_col)-1] = 'H'
                print_board(board)
                guesses_left -= 1
            """
            If the guessed row and column are equal to a H on the board,
            the hit ship is removed from the ships_to_hit list.
            User is informed, and remaining number of ships is displayed.
            """
            if board[int(guess_row)-1][int(guess_col)-1] == 'H':
                ships_to_hit.remove(hit_ship)
                guess_correct = True
                print('\nHit!')
                print("\nNumber of ships left:", len(ships_to_hit))
                break

        if not guess_correct:
            if board[int(guess_row)-1][int(guess_col)-1] == 'H' \
                    or board[int(guess_row)-1][int(guess_col)-1] == 'X':
                print_board(board)
                print('\nYou have made that guess already!\n')
            else:
                board[int(guess_row)-1][int(guess_col)-1] = 'X'
                print_board(board)
                print('\nMiss!\n')
                guesses_left -= 1
                print(f'\nNumber of guesses left: {guesses_left}\n')
        if len(ships_to_hit) == 0:
            print('\nCongratulations! You all sank my battleships!\n')
            print_end()
            break
        if guesses_left == 1:
            print('Oh, no! You lost!')
            print_end()
            break


make_guesses()
