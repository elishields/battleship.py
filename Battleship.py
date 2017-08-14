# import the randint class
from random import randint

# print game instructions
print(
        "\nLet's play Battleship!"
        + "\nThere are 3 hidden ships."
        + "\nShip size is 1 dot."
        + "\n'.' is unattacked ocean."
        + "\n'X' is missed shots."
        + "\nGuess a row, then a column."
        + "\nYou get 4 guesses."
        )

# prompt difficulty selection
difficulty = input("How daring are you? Type 'easy', 'medium', or 'hard'.\n")
if difficulty.lower() == "easy":
    board_size = 4
elif difficulty.lower() == "medium":
    board_size = 5
elif difficulty.lower() == "hard":
    board_size = 6
else:
    board_size = 5

# create empty list
board = []

# append board_size number of columns and rows of '.' to board[] list
for x in range(board_size):
    board.append(["."] * board_size)

# prints each row of board[] list with column items joined by a blank space
def print_board(board):
    for row in board:
        print(" ".join(row))

# calls print_board function with board[] list as argument
print_board(board)

# generate a random row position for a new battleship
def random_row(board):
    return randint(0, len(board) - 1)

# randomly assign a column position for a new battleship
def random_col(board):
    return randint(0, len(board[0]) - 1)

# set battleship positions using random generator functions
ship_row1 = random_row(board)
ship_col1 = random_col(board)
ship_row2 = random_row(board)
ship_col2 = random_col(board)
ship_row3 = random_row(board)
ship_col3 = random_col(board)

# prompt user to guess a row and column for up to 4 turns
for turn in range(4):
    turnCount = turn + 1
    print("Turn", turnCount)
    guess_row = int(input("Guess Row: "))
    guess_row -= 1
    guess_col = int(input("Guess Col: "))
    guess_col -= 1
    # if user correctly guesses the ship location, print a win message and break the guessing loop
    if (guess_row == ship_row1 and guess_col == ship_col1) \
            or (guess_row == ship_row2 and guess_col == ship_col2) \
            or (guess_row == ship_row3 and guess_col == ship_col3):
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = '!'
        print_board(board)
        break
    else:
        # else if user guess is not on the board, notify user of board size
        if (guess_row < 0 or guess_row > board_size) or (guess_col < 0 or guess_col > board_size):
            print("Oops, that's not even in the ocean.\nGuess row and column location's between 1 and " + str(board_size) + ".\n")
        # else if current guess is a previous guess, notify user
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.\n")
        # else if user guess is not an integer
        elif (isinstance(guess_row, int)) and (isinstance(guess_col, int)) is False:
            print("You didn't guess an integer number between 1 and 4.\nTry again.")
        # else if user guess misses the ship location, print a miss message
        else:
            print("You missed my battleship!\n")
            board[guess_row][guess_col] = "X"
        # if user is on their 4th guess, print game over
        if turn == 4:
            print("Game Over.\nYou Lose.\nNeener neener neener nana nana nana!")
        print_board(board)
