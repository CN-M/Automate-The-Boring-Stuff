# A Tic Tac Toe game

import pprint as pp

TheBoard = {'Low-L':' ', 'Low-M':' ', 'Low-R':' ', 'Mid-L':' ', 'Mid-M': ' ', 'Mid-R':' ', 'Top-L':' ', 'Top-M': ' ','Top-R':' ' }

#pp.pprint(TheBoard)

TheBoard["Top-R"] = 'X'
TheBoard["Top-M"] = 'X'
TheBoard["Top-L"] = 'X'

TheBoard['Mid-L'] = 'O'
TheBoard['Low-M'] = 'O'
TheBoard['Low-R'] = 'O'


def printBoard(board):
    print(board['Top-L'] + '|' + board['Top-M'] + '|' + board['Top-R'])
    print('------')
    print(board['Mid-L'] + '|' + board['Mid-M'] + '|' + board['Mid-R'])
    print('------')
    print(board['Low-L'] + '|' + board['Low-M'] + '|' + board['Low-R'])


printBoard(TheBoard)
c = type('Hi')
print(c)