"""
Tic Tac Toe Player
"""

import math
from queue import Empty
import copy

X = "X"
O = "O"
EMPTY = None

#the tictactoe board is defined as list contaning 3 lists for each row
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
    totalx = 0
    totalo = 0

    for eachrow in board:
        for eachcell in eachrow :
            if eachcell == X :
                totalx += 1
            elif eachcell == O :
                totalo += 1
    
    
    if totalx == totalo :
        return X
    elif totalx > totalo :
        return O
    else :
        return O


    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY :
                actions.add((i,j))
    return actions 


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    newboard = copy.deepcopy(board)

    newboard[i][j] = player(board)

    return newboard 

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #horizontal check

    for eachrow in board:
        if eachrow[0] == eachrow[1] and eachrow[1] == eachrow [2] :
            return eachrow[0]

    #vertical check 

    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] :
            return board[0][i]
    
    #diagnol check 
    i = 0

    if board[i][i] == board[i+1][i+1] and board[i+1][i+1] == board[i+2][i+2] :
        return board[i][i]

    elif  board[0][2] == board[1][1] and board[1][1] == board[2][0] :
        return board[0][2]

    else:
        return None

    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    def stillrunning(board) :
        for eachrow in board:
            for eachcell in eachrow:
                if eachcell == EMPTY :
                    return True 

    if winner(board) == X or winner(board) == O :
        return True
    elif stillrunning(board) :
        return False
    else: 
        return True




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) :
        if winner(board) == X:
            return 1
        elif winner(board) == O :
            return -1
        else:
            return 0

    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) :
        return None
    else:
        
        if player(board) == X :
            value,move = MaxValue(board)
            return move

        else :
            value,move = MinValue(board)
            return move

def MaxValue(board) :
    v = float('-inf')
    move=None

    if terminal(board):
        return utility(board),None

    for action in actions(board):
        #v = max(v, MinValue(result(board, action)))
        x,y  = MinValue(result(board, action))
        if x > v:
            v = x
            move = action
            if v == 1:
                return v, move

    return v, move


        
def MinValue(board) :
    v = float('inf')
    move = None

    if terminal(board):
        return utility(board),None

    for action in actions(board):
        #v = min(v, MaxValue(result(board, action)))
        x, y = MaxValue(result(board, action))
        if x < v:
            v = x
            move = action
            if v == -1:
                return v, move

    return v, move
    

        