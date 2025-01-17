rows, cols = map(int, input().split())
matrix = [[x for x in input()] for _ in range(rows)]
movement_commands = input()

# Map for directions
directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

player_won = False
player_dead = False


for move in movement_commands:
    bunny_positions = []
    # Determining player and bunny starting positions:
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'P':
                player_curr_pos = (i, j)
            elif matrix[i][j] == 'B':
                bunny_curr_pos = (i, j)
                bunny_positions.append(bunny_curr_pos)

    # Move the player
    new_player_row = player_curr_pos[0] + directions[move][0]
    new_player_col = player_curr_pos[1] + directions[move][1]

    # Check if player escapes
    if not (0 <= new_player_row < rows and 0 <= new_player_col < cols):
        player_won = True
        player_won_coords = [player_curr_pos[0], player_curr_pos[1]]
        matrix[player_curr_pos[0]][player_curr_pos[1]] = '.'

    # Check if player bumps into a bunny
    if 0 <= new_player_row < rows and 0 <= new_player_col < cols:
        if matrix[new_player_row][new_player_col] == 'B':
            player_dead = True
            player_dead_coords = [new_player_row, new_player_col]
    # If not bumping into bunny, update player pos
        if 0 <= new_player_row < rows and 0 <= new_player_col < cols:
            matrix[player_curr_pos[0]][player_curr_pos[1]] = '.'
            matrix[new_player_row][new_player_col] = 'P'

    # Spread bunnies
    new_bunny_positions = []
    for bunny_row, bunny_col in bunny_positions:
        for dr, dc in directions.values():
            new_row, new_col = bunny_row + dr, bunny_col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                matrix[new_row][new_col] = '.'
                new_bunny_positions.append((new_row, new_col))

    # Update matrix with new bunnies
    for br, bc in new_bunny_positions:
        matrix[br][bc] = 'B'

    # Check if the player is now on a bunny
    if matrix[new_player_row][new_player_col] == 'B':
        player_dead = True
        player_dead_coords = [new_player_row, new_player_col]

    if player_won or player_dead:
        break

for row in matrix:
    print(''.join(row))

if player_won:
    print(f"won: {' '.join(map(str, player_won_coords))}")
    exit()
if player_dead:
    print(f"dead: {' '.join(map(str, player_dead_coords))}")