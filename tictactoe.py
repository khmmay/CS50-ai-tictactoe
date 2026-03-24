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
    num_X=0
    num_O=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                num_X+=1
            if board[i][j]==O:
                num_O+=1

    if num_X>num_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    mov_list=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                mov_list.append((i,j))

    return mov_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action==None:
        return board
    if action not in actions(board):
        raise AssertionError
    board1=copy.deepcopy(board)
    board1[action[0]][action[1]] = player(board)
    return board1


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[1][i] == board[2][i] == board[0][i] == X:
            return X
        if board[1][i] == board[2][i] == board[0][i] == O:
            return O
        if board[i][1] == board[i][2] == board[i][0] == X:
            return X
        if board[i][1] == board[i][2] == board[i][0] == O:
            return O
        if board[1][1] == board[2][2] == board[0][0] == X:
            return X
        if board[1][1] == board[2][2] == board[0][0] == O:
            return O
        if board[0][2] == board[1][1] == board[2][0] == X:
            return X
        if board[0][2] == board[1][1] == board[2][0] == O:
            return O
    return None   
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    else:
        if any(cell is None for row in board for cell in row):
            return False
        else:
            return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==None:
        return 0
    elif winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    scores=[]
    if player(board)==X:
        for a in actions(board):
            scores.append(min_val(result(board,a), alpha=-math.inf, beta=math.inf))
        return actions(board)[scores.index(max(scores))]
    else:
        for a in actions(board):
            scores.append(max_val(result(board,a), alpha=-math.inf,beta=math.inf))
        return actions(board)[scores.index(min(scores))]
def max_val(board,alpha ,beta):

    if terminal(board):
        return utility(board)
    v = -math.inf
    for a in actions(board):
        v = max(v, min_val(result(board,a),alpha,beta))
        alpha = max(alpha,v)
        if alpha >= beta:
            break
    return v

def min_val(board,alpha,beta):
    if terminal(board):
        return utility(board)
    v = math.inf
    for a in actions(board):
        v = min(v, max_val(result(board,a),alpha,beta))
        beta = min(v,beta)
        if alpha >=beta:
            break
    return v