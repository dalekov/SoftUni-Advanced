def setup():
    """Asks for player names and signs."""
    global player_one, player_two

    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")

    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

    while player_one_sign not in ["X", "O"]:
        player_one_sign = input("Invalid input! Please choose 'X' or 'O': ")
    player_two_sign = 'X' if player_one_sign == 'O' else 'O'

    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]

    print("Signs:")
    print(f"{player_one_name} - {player_one_sign}")
    print(f"{player_two_name} - {player_two_sign}")

    print("This is the numeration of the board:")
    print("|  1  |  2  |  3  |")
    print("|  4  |  5  |  6  |")
    print("|  7  |  8  |  9  |")

    print(f"{player_one_name} starts first!")

def draw_board(field):
    """Draws the board after each player turn."""
    for row in field:
        print("|  ", end="")
        print("  |  ".join([str(x) for x in row]), end="")
        print("  |")


def check_win(current_player, field):
    global loop
    """Checks if there is a winning position on the field."""

    # Check columns:
    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] != " ":
            loop = False
            print(f"{current_player[0]} won!")
            break

    # Check row:
    for row in range(3):
        if field[row][0] == field[row][1] == field[row][2] != " ":
            loop = False
            print(f"{current_player[0]} won!")
            break

    # Check diagonals:
    if (field[0][0] == field[1][1] == field[2][2] != " ") or (field[0][2] == field[1][1] == field[2][0] != " "):
        loop = False
        print(f"{current_player[0]} won!")



def play(current_player, field):
    """Main game logic."""
    chosen_position = int(input(f"{current_player[0]}, choose a free position [1-9]: "))

    while chosen_position not in range(1, 10):
        chosen_position = int(input(f"Invalid position! {current_player}, choose a free position [1-9]: "))

    # Calculate coords of the chosen field in the board:
    row = (chosen_position - 1) // 3
    col = (chosen_position - 1) % 3

    # Loop until the player selects a free position:
    while field[row][col] != " ":
        chosen_position = int(input(f"Position taken! {current_player}, choose a free position [1-9]: "))
        row = (chosen_position - 1) // 3
        col = (chosen_position - 1) % 3

    # If position is free, place the current player's sign:
    field[row][col] = current_player[1]

    # Draw the current board:
    draw_board(field)
    # Check if the current player has won:
    check_win(current_player, field)

board = [[" ", " ", " "] for _ in range(3)]
player_one = None
player_two = None

setup()
current = player_one
other = player_two

loop = True
while loop:
    play(current, board)
    current, other = other, current
