import math
from docx import Document
import sys
import builtins


print_statements = []


def print_board(board):
    print(" 1   2   3")
    for i, row in enumerate(board):
        print(f"{i + 1} {' | '.join(row)}")
        if i < 2:
            print(" ---|---|---")



def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_valid_move(row, col, board):
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        return True
    print("Invalid move. The number should be between 1 and 3 and should be empty")
    return False

def is_board_full(board):
    for row in board:
        if any(cell == " " for cell in row):
            return False
    return True


def minimax(board, depth, is_maximizing, alpha, beta):


    scores = {
        "X": -2,
        "O": 20,
        "tie": 0
    }

    winner = None
    if check_winner(board, "X"):
        winner = "X"
    elif check_winner(board, "O"):
        winner = "O"

    if winner:
        return scores[winner]

    if is_board_full(board):
        return scores["tie"]


    if is_maximizing:
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)

                    board[i][j] = " "
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break

        return alpha

    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break


        return beta

def find_best_move(board):


    best_move = None
    best_score = -math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False, -5, 40)

                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def main():
    board = [[" " for i in range(3)] for i in range(3)]
    game_over = False
    current_player = "X"
    print("Welcome to Steve's Tic-Tac-Toe")

    while not game_over:
        print_board(board)

        if current_player == "X":
            try:
                row = int(input(f"{current_player} Please select a row -  1, 2, 3: ")) - 1
                col = int(input(f"{current_player} Please choose a column - 1, 2, 3: ")) - 1

                if is_valid_move(row, col, board):
                    board[row][col] = current_player
                    if check_winner(board, current_player):
                        print(f"{current_player} wins!")
                        print_board(board)
                        game_over = True
                    elif is_board_full(board):
                        print("It's a tie!")
                        print_board(board)
                        game_over = True
                    else:
                        current_player = "O"

            except ValueError:
                print("Please input a number between 1-3")
                continue
        else:
            print("AI's turn (O)")
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = "O"
            if check_winner(board, current_player):
                print(f"{current_player} wins!")
                print_board(board)
                game_over = True
            elif is_board_full(board):
                print("It's a tie!")
                print_board(board)
                game_over = True
            else:
                current_player = "X"

        with open("print_statements.txt", "w") as f:
                    for statement in print_statements:
                        f.write(statement + '\n')

if __name__ == "__main__":
    main()
