board = input("Enter cells: ")

game_states = {
    0: "Game not finished",
    1: "Draw",
    2: "X wins",
    3: "O wins",
    4: "Impossible",
}

print("---------")
print("| " + " ".join(board[0:3]) + " |")
print("| " + " ".join(board[3:6]) + " |")
print("| " + " ".join(board[6:9]) + " |")
print("---------")

win_combos = [[board[0], board[1], board[2]],
              [board[3], board[4], board[5]],
              [board[6], board[7], board[8]],
              [board[0], board[3], board[6]],
              [board[1], board[4], board[7]],
              [board[2], board[5], board[8]],
              [board[0], board[4], board[8]],
              [board[2], board[4], board[6]]]

x_moves = board.count("X")
o_moves = board.count("O")
is_full_board = x_moves + o_moves == 9
x_wins = len([c for c in win_combos if c.count("X") == 3])
o_wins = len([c for c in win_combos if c.count("O") == 3])

if x_wins and o_wins or max(x_moves, o_moves) - min(x_moves, o_moves) >= 2:
    print(game_states.get(4))
elif not x_wins and not o_wins and is_full_board:
    print(game_states.get(1))
elif x_wins:
    print(game_states.get(2))
elif o_wins:
    print(game_states.get(3))
else:
    print(game_states.get(0))
