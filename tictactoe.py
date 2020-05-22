"""
Tic Tac Toe Player
"""

import math
import copy
from random import sample, choice

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

def open_cells(board):
    open_cells = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == None:
                open_cells += 1
    return open_cells

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if open_cells(board) == 0:
        return "terminal"
    elif open_cells(board) % 2 == 0:
        return O
    else:
        return X
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == None:
                square = (i,j)
                moves.add(square)
    if len(moves) > 0:
        return moves
    else:
        return "terminal"

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != None:
        raise Exception("Invalid action")
    
    board1 = copy.deepcopy(board)
    player_turn = player(board)

    board1[action[0]][action[1]] = player_turn
    return board1

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i][0] == X and board [i][1] == X and board[i][2] == X:
            return X
    for i in range(len(board)):
        if board[0][i] == X and board [1][i] == X and board [2][i] == X:
            return X
    if board[0][0] == X and board [1][1] == X and board[2][2] == X:
        return X
    
    if board[0][2] == X and board [1][1] == X and board[2][0] == X:
         return X
    
    for i in range(len(board)):
        if board[i][0] == O and board [i][1] == O and board[i][2] == O:
            return O
    for i in range(len(board)):
        if board[0][i] == O and board [1][i] == O and board [2][i] == O:
            return O
    if board[0][0] == O and board [1][1] == O and board[2][2] == O:
        return O
    if board[0][2] == O and board [1][1] == O and board[2][0] == O:
         return O  

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O or open_cells(board) == 0:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    if player(board) == X:
        if board == initial_state():
            a = (0,0)
            b = (0,2)
            c = (2,0)
            d = (2,2)
            first_move = choice([a,b,c,d])
            return first_move
        for action in actions(board):
            if min_value(result(board, action)) == 1:
                return action
        for action in actions(board):
            if min_value(result(board, action)) == 0:
                return action
    if player(board) == O:
        for action in actions(board):
            if max_value(result(board, action)) == -1:
                return action
        for action in actions(board):
            if max_value(result(board, action)) == 0:
                return action
            
def max_value(board):
    if terminal(board) == True:
        return utility(board)
    v = -2
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v

def min_value(board):
    if terminal(board) == True:
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v