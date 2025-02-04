ROWS = 6
COLS = 7

player_one = None
player_two = None


def draw_board(field):
    for row in field:
        print(row)

def check_winner(current_player, field):
    # Check rows
    for row in range(ROWS):
        for col in range(COLS - 3):
            if field[row][col] == field[row][col + 1] == field[row][col + 2] == field[row][col + 3] == current_player[1]:
                return True


    # Check cols
    for row in range(ROWS - 3):
        for col in range(COLS):
            if field[row][col] == field[row + 1][col] == field[row + 2][col] == field[row + 3][col] == current_player[1]:
                return True

    # Check falling diagonal
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if field[row][col] == field[row + 1][col + 1] == field[row + 2][col + 2] == field[row + 3][col + 3] == current_player[1]:
                return True

    # Check rising diagonal
    for row in range(3, ROWS):  # Start from row 3 to avoid out-of-bounds errors
        for col in range(COLS - 3):  # Ensure valid diagonal check
            if (field[row][col] == field[row - 1][col + 1] ==
                    field[row - 2][col + 2] == field[row - 3][col + 3] == current_player[1]):
                return True

    # If no winner found, continue:
    return False

def is_draw(field):
    for row in field:
        if 0 in row:
            return False
    return True


def setup():
    global player_one, player_two

    player_one_name = input("Player 1 name: ")
    player_two_name = input("Player 2 name: ")

    player_one = [player_one_name, 1]
    player_two = [player_two_name, 2]

    print("Signs:")
    print(f"{player_one_name} - 1")
    print(f"{player_two_name} - 2")

    draw_board(board)


def play(current_player, field):
    global current, other
    while True:
        try:
            column = int(input(f"{current_player[0]}, please choose a column [1-7]: ")) - 1
            if column < 0 or column >= COLS:
                print("Invalid column! Please choose a number between 1 and 7.")
                continue
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        # Check if the column is full
        if field[0][column] != 0:
            print("Column is full! Please choose another one.")
            continue

        # Place the piece in the lowest available row
        for row in range(ROWS - 1, -1, -1):
            if field[row][column] == 0:
                field[row][column] = current_player[1]
                draw_board(field)
                return




board = []
for i in range(ROWS):
    board.append([])
    for _ in range(COLS):
        board[i].append(0)

setup()
current = player_one
other = player_two

loop = True
while loop:
    play(current, board)
    if check_winner(current, board):
        print(f"{current[0]} wins!")
        loop = False
    elif is_draw(board):
        loop = False
        print("Tie!")
    current, other = other, current