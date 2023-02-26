import random

def print_board(board):
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want to be X or O? ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position-1] = marker

def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[0] == mark and board[4] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark))

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position-1] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')

print("Welcome to Tic Tac Toe!")
while True:
    board = [' '] * 9
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input("Are you ready to play? Enter Yes or No.")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            print_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

    if win_check(board, player1_marker):
        print(board)
