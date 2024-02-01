"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx = 0
    counto = 0
    if winner(board) is None:
        for row in board:
            for cell in row:
                if cell == X:
                    countx += 1
                elif cell == O:
                    counto += 1

        if countx > counto:
            return O
        else:
            return X
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] != X and board[i][j] != O:
                action.add((i,j))
    
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    board_copy = copy.deepcopy(board)
    i,j = action
    
    if i<0 or i>2 or j<0 or j>2:
        raise Exception("Not valid Action")
    else:
        if (current_player := player(board)) is not None:
            board_copy[i][j]=current_player
    
    return board_copy


def checkRow(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1]==board[i][2]:
            return board[i][1]
    return None


def checkCol(board):
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
    return None


def checkDiagonals(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winnerPlayer = checkRow(board)
    if winnerPlayer is None:
        winnerPlayer = checkCol(board)
    if winnerPlayer is None:
        winnerPlayer = checkDiagonals(board)
    return winnerPlayer
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winnerPlayer = winner(board)
    if winnerPlayer is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] != X and board[i][j] != O:
                return False
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerPlayer = winner(board)
    if winnerPlayer is None:
        return 0
    if winnerPlayer == X:
        return 1
    if winnerPlayer == O:
        return -1

    

def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)
    if current_player == X:
        return max_value(board)[1]
    return min_value(board)[1]

def max_value(board):
    if terminal(board):
        return (utility(board), None)
    best_move = None
    v = float("-inf") # negative infinity
    for action in actions(board):
        result_board = result(board, action)
        min_val = min_value(result_board)[0]
        if min_val > v:
            v = min_val
            best_move = action
    return (v, best_move)


def min_value(board):
    if terminal(board):
        return (utility(board), None)
    best_move = None
    v = float("inf")
    for action in actions(board):
        result_board = result(board, action)
        max_val = max_value(result_board)[0]
        if max_val < v:
            v = max_val
            best_move = action
    return (v, best_move)