from prettytable import PrettyTable, ALL

table = PrettyTable()
table.hrules = ALL
table.header = False
table.padding_width = 3


board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

table.add_rows(board)
print(table)


# Function to check if all elements in a row are the same
def check_row(row):
    return all(cell == row[0] for cell in row)

# Function to check if all elements in a column are the same
def check_column(column_index):
    return all(row[column_index] == board[0][column_index] for row in board)

# Function to check if all elements in a diagonal position are the same
def check_diagonally():
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return True
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return True
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return True
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return True


player = input("Select a player(X or O): ")
game_on = True
n = 2
while game_on:
    turn = int(input("Enter your move: "))
    if n % 2 == 0:
        for row in board:
            if turn in row:
                row[row.index(turn)] = "X"
    else:
        for row in board:
            if turn in row:
                row[row.index(turn)] = "O"

    table.clear_rows()
    table.add_rows(board)
    print(table)
    n += 1

    # Check for a winning condition in any row or column
    for i in range(len(board)):
        if check_row(board[i]) or check_column(i):
            print(f"Player {player} wins!")
            game_on = False
            break
    if check_diagonally():
        print(f"Player {player} wins!")
        game_on = False
        break
