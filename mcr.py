def is_win(board):
    win = False
    # Check rows
    if board[0][0] == board[0][1] == board[0][2] and (board[0][0] == 'X' or board[0][0] == 'O'):
        win = True
    if board[1][0] == board[1][1] == board[1][2] and (board[1][0] == 'X' or board[1][0] == 'O'):
        win = True
    if board[2][0] == board[2][1] == board[2][2] and (board[2][0] == 'X' or board[2][0] == 'O'):
        win = True
    # Check columns
    if board[0][0] == board[1][0] == board[2][0] and (board[0][0] == 'X' or board[0][0] == 'O'):
        win = True
    if board[0][1] == board[1][1] == board[2][1] and (board[0][1] == 'X' or board[0][1] == 'O'):
        win = True
    if board[0][2] == board[1][2] == board[2][2] and (board[0][2] == 'X' or board[0][2] == 'O'):
        win = True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and (board[0][0] == 'X' or board[0][0] == 'O'):
        win = True
    if board[0][2] == board[1][1] == board[2][0] and (board[0][2] == 'X' or board[0][2] == 'O'):
        win = True
    return win

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1_symbol = 'X'
    player2_symbol = 'O'
    is_player2_turn = False  # False for Player 1's turn, True for Player 2's turn. Player 1 starts.
    print("X = Player 1")
    print("O = Player 2")
    for turn_count in range(9):
        is_player2_turn = not is_player2_turn  # Switch turns
        if not is_player2_turn:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ")
        row, col = map(int, input().split())
        row -= 1
        col -= 1
        if not is_player2_turn:
            board[row][col] = player1_symbol
        else:
            board[row][col] = player2_symbol
        if is_win(board):
            print("Win!")
            break  # Terminate the game
        if turn_count == 8:  # All cells have been filled
            print("Tie!")
        # Show the game board
        for row in board:
            print(" ".join(row))

if __name__ == "__main__":
    main()
