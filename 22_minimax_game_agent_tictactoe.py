# """Practical 22: Game-playing agent using Minimax (Tic-Tac-Toe).
# X is the AI, O is the opponent. Minimax assumes both play optimally.
# """
# board = [" "] * 9
# WIN_LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
#              (1,4,7),(2,5,8),(0,4,8),(2,4,6)]

# def winner(b):
#     for a, c, d in WIN_LINES:
#         if b[a] != " " and b[a] == b[c] == b[d]:
#             return b[a]
#     return None

# def minimax(b, is_maximizing):
#     result = winner(b)
#     if result == "X": return 1
#     if result == "O": return -1
#     if " " not in b: return 0
#     if is_maximizing:
#         best = float("-inf")
#         for i in range(9):
#             if b[i] == " ":
#                 b[i] = "X"
#                 best = max(best, minimax(b, False))
#                 b[i] = " "
#         return best
#     best = float("inf")
#     for i in range(9):
#         if b[i] == " ":
#             b[i] = "O"
#             best = min(best, minimax(b, True))
#             b[i] = " "
#     return best

# def choose_move(b):
#     best_score, best_index = float("-inf"), None
#     for i in range(9):
#         if b[i] == " ":
#             b[i] = "X"
#             score = minimax(b, False)
#             b[i] = " "
#             if score > best_score:
#                 best_score, best_index = score, i
#     return best_index

# # Demonstrate the AI's first move from an empty board.
# move = choose_move(board)
# board[move] = "X"
# print("AI chooses position:", move + 1)
# for i in range(0, 9, 3):
#     print("|".join(board[i:i+3]))




"""Tic-Tac-Toe using Minimax Algorithm."""

board = [" "] * 9

# All possible winning positions
win = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

# Check winner
def check_winner():
    for a, b, c in win:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

# Minimax algorithm
def minimax(is_ai):
    result = check_winner()

    if result == "X":
        return 1
    if result == "O":
        return -1
    if " " not in board:
        return 0

    if is_ai:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best

    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

# Find AI's best move
def best_move():
    best_score = -100
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

# Display board
move = best_move()
board[move] = "X"

print("AI chooses position:", move + 1)

for i in range(0, 9, 3):
    print("|".join(board[i:i+3]))
