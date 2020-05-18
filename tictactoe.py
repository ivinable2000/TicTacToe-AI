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
    turn = 0
    for row in board:
        for col in row:
            if col == X:
                turn += 1
            elif col == O:
                turn -= 1
    if turn == 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = []
    row = col = 0
    while row < 3:
        col = 0
        while col < 3:
            if board[row][col] == EMPTY:
                actionSet.append([row, col])
            col += 1
        row += 1
    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise NotImplementedError
    newBoard = copy.deepcopy(board)
    input = player(board)
    newBoard[action[0]][action[1]] = input

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0]  
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != EMPTY:
        return board[2][0]  
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]  
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]  
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[1][1] != EMPTY:
        return board[0][2]  

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
        
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    utility = winner(board)
    if not utility:
        return 0
    elif utility == X:
        return 1
    else:
        return -1

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        move = optimalMove(board, -2, 2)
        return move[1]

def optimalMove(board, alpha, beta):
    if terminal(board):
        return [utility(board),]
    
    # Maximizing Agent
    if player(board) == X:
        maxScore = -2
        moves = actions(board)
        maxMove = moves[0]
        for move in moves:
            newBoard = result(board, move)
            score = optimalMove(newBoard, alpha, beta)
            if score[0] > maxScore:
                maxScore = score[0]
                maxMove = move
            alpha = max(alpha, score[0])
            if beta <= alpha:
                break
        return [maxScore, maxMove]
    # Minimizing Agent
    else:
        minScore = 2
        moves = actions(board)
        minMove = moves[0]
        for move in moves:
            newBoard = result(board, move)
            score = optimalMove(newBoard, alpha, beta)
            if score[0] < minScore:
                minScore = score[0]
                minMove = move
            beta = min(beta, score[0])
            if beta <= alpha:
                break
        return [minScore, minMove]
