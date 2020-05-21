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
    
    board1 =copy.deepcopy(board)
    player_turn = player(board)

    board1[action[0]][action[1]] = player_turn
    return board1

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


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
    raise NotImplementedError
