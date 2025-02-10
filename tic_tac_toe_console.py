from random import randrange

def init_board():
    global current_player
    board = [['' for x in range(3)] for i in range(3)]
    pos = 1
    for row in range(3):
        for column in range(3):
            board[row][column] = pos
            pos += 1
    
    board[1][1] = 'X'
    current_player = 'O'
    return board
    
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------' * 3, '+', sep='')
    for row in range(3):
        print('|       ' * 3, '|', sep='')
        for col in range(3):
            print('|  ', str(board[row][col])+ '   ', end='')
        print('|')
        print('|       ' * 3, '|', sep='')
        print('+-------' * 3, '+', sep='')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    turn_ok = False
    
    while not turn_ok:
        move = input('Enter a move (1 to 9) : ')
        
        if len(move) != 1 or move <= '0' or move > '9':
            print("Your move isn't correct, retry please ")
            continue
        
        move = int(move) - 10
        row = move // 3
        col = move % 3
        
        if board[row][col] in ['O', 'X']:
            print("Your move isn't correct, this square is occupied, please retry again !")
            continue

        turn_ok = not turn_ok
        board[row][col] = 'O'


def free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['O', 'X']:
                free_squares.append((row, column))
    return free_squares


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # check rows
    for row in range(3):
        if board[row][0] == sign and board[row][0] == board[row][1] and board[row][1]==board[row][2]:
            return sign
    
    # check columns
    for column in range(3):
        if board[0][column] == sign and board[0][column] == board[1][column] and board[0][column]==board[2][column]:
            return sign
    
    # check diagonals
    if board[0][0] == sign and board[0][0] == board[1][1] and board[1][1] == board[2][2] or \
        board[0][2] == sign and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return sign

    return None

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_squares = free_fields(board)

    free_squares_length = len(free_squares)
    if free_squares_length > 0:
        random = randrange(free_squares_length)
        row, col = free_squares[random] 
        board[row][col] = 'X'
        
def start_the_game():
    game_status = '0'
    while game_status != '-1':
        print('*-----------------------------*')
        print('* Welcome to TicTacToe game!', ' *')
        print('* Enter 0 to start the game.', ' *')
        print('* Enter -1 to end the game.', '  *')
        print('*-----------------------------*')

        game_status = input('Enter your choice : ')

        if type(game_status) != "<class 'str'>" and game_status not in ['0', '-1']:
            print('Please enter 0 or -1')
            continue

        if game_status == '-1':
            break
        
        # main program
        board = init_board()
        play(board)
        display_board(board)

        if winner != None :
            print()
            print('Yohoo ! The player', winner, 'won the game !')
            print()
        else:
            print('Tie game !') 
            
            print('Tie game !') 
def play(board):
    free_squares = len(free_fields(board))
    global winner
    global current_player
    
    while free_squares != 0:
        display_board(board)
        
        if current_player == 'O':
            # player turn
            enter_move(board)
        else:
            # computer turn
            draw_move(board)
        
        game_winner = victory_for(board, current_player)
        
        if game_winner != None:
            winner = game_winner
            break
        else:
            if current_player == 'O':
                current_player = 'X'
            else:
                current_player = 'O'

        free_squares = len(free_fields(board))
        
start_the_game()
