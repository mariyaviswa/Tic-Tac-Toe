def create_board() -> list:
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\n")
    print("-" * 10)
    for b in board:
        print(" | ".join(b))
        print("-" * 10)
    print("\n")

def get_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter col (0-2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("❌ Row and column must be between 0 and 2.")
        except ValueError:
            print("❌ Please enter valid numbers.")
def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print("Cell is already taken. Try again.")
        return False

def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

def check_winner(board, player):
    # Check row wise 
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check column wise
    for i in range(3):
        if all(board[j][i] == player for j in range(3)):
            return True
    
    # Check diagonals left to right
    if all(board[i][i] == player for i in range(3)):
        return True
    # Check diagonals right to left
    if all(board[2-i][i] == player for i in range(2, -1, -1)):
        return True
    
    return False
board = create_board()
print_board(board=board)

current_player = "X"

while True:
    # print the board
    print_board(board=board)
    row, col = get_move(current_player)
    if make_move(board=board, row=row, col=col, player=current_player):
        # Check winner
        if check_winner(board=board, player=current_player):
            print_board(board=board)
            print(f"player {current_player} wins!.")
            break
        # Chec if board is full or not 
        if is_board_full(board=board):
            print_board(board=board)
            print("🤝 It's a draw!")
            break
        # switch player
        current_player = 'O' if current_player == 'X' else 'X'