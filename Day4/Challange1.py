import numpy as np
boards=[]
def allEqual(arr):
    return arr.count(arr[0]) == len(arr)

def getBoards(data):
    while True:      
        board = [["X" for i in range(5)] for j in range(5)]
        for i in range(0, 5):
            row = data.readline().split()
            if len(row) != 0:
                board[i] = [int(item) for item in row]
            else:
                return boards
        boards.append(board)
        data.readline() #blank line
        
        #print(board)
def getColumn(board, colNumber):
    return [row[colNumber] for row in board]
def markNumber(board, number):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == number:
                board[i][j] = 'X'
def checkRowWin(row):
    return allEqual(row)
def checkColWin(col):
    return allEqual(col)
def checkBoard(board, number):
    for i in range(0, 5):
        rowWin = checkRowWin(board[i])
        colWin = checkColWin(getColumn(board, i))
        if rowWin or colWin:
            return True
    
def playBingo(numbers, boards):
    for number in numbers:
        #print(number)
        for board in boards:
            markNumber(board, number)
            winner = checkBoard(board, number)
            if winner:
                return number, board
                
def calcAnswer(number, board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 'X':
                total += board[i][j]
    return total * number
with open('Data.txt') as data:
    #diagnostics = data.readlines()
    numbers = [int(item) for item in data.readline().split(",")]
    data.readline() #blank line
    boards = getBoards(data)
    winningNumber,winningBoard = playBingo(numbers, boards)
    print("Winning number:", winningNumber)
    print("Winning board:", winningBoard)
    print(calcAnswer(winningNumber, winningBoard))
    