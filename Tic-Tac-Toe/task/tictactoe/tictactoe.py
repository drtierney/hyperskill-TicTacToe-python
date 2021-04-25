import re

game_states = {
    0: "Game not finished",
    1: "Draw",
    2: "X wins",
    3: "O wins",
    4: "Impossible",
}


def print_board(board):
    border = "-" * 9
    print(border)
    print(f"| {the_board[0][0]} {the_board[0][1]} {the_board[0][2]} |")
    print(f"| {the_board[1][0]} {the_board[1][1]} {the_board[1][2]} |")
    print(f"| {the_board[2][0]} {the_board[2][1]} {the_board[2][2]} |")
    print(border)


def make_move(move, board, symbol):
    if not re.search(r'\d\s\d', move):
        print("You should enter numbers!")
        return False

    x = int(move[0])
    y = int(move[2])
    if x > 3 or x < 1 or y > 3 or y < 1:
        print("Coordinates should be from 1 to 3!")
        return False

    i = x - 1
    j = y - 1
    if board[i][j] in ["X", "O"]:
        print("This cell is occupied! Choose another one!")
        return False
    board[i][j] = symbol
    return True


def check_game_state(board):
    win_states = [[board[0][0], board[0][1], board[0][2]],
                  [board[1][0], board[1][1], board[1][2]],
                  [board[2][0], board[2][1], board[2][2]],
                  [board[0][0], board[1][0], board[1][0]],
                  [board[0][1], board[1][1], board[2][1]],
                  [board[0][2], board[1][2], board[2][2]],
                  [board[0][0], board[1][1], board[2][2]],
                  [board[0][2], board[1][1], board[2][0]]]
    
    x_moves = sum(x.count("X") for x in board)
    o_moves = sum(o.count("O") for o in board)

    is_full_board = x_moves + o_moves == 9
    x_wins = len([c for c in win_states if c.count("X") == 3])
    o_wins = len([c for c in win_states if c.count("O") == 3])

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


initial_state = input("Enter cells: ").replace("_", " ")

the_board = [[initial_state[0], initial_state[1], initial_state[2]],
             [initial_state[3], initial_state[4], initial_state[5]],
             [initial_state[6], initial_state[7], initial_state[8]]]

print_board(the_board)
can_make_move = False

while not can_make_move:
    user_move = input("Enter the coordinates: ")
    can_make_move = make_move(user_move, the_board, "X")
print_board(the_board)
