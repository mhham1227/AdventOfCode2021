boards=[]
def allEqual(arr):
    #Check if count of first item in list is == the total number of items
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
                
def checkRowOrColWin(row):
    return allEqual(row)
    
def checkBoard(board, number):
    for i in range(0, 5):
        rowWin = checkRowOrColWin(board[i])
        colWin = checkRowOrColWin(getColumn(board, i))
        if rowWin or colWin:
            return True
    
def playBingo(numbers, boards):
    for number in numbers:
        #Need to mark all of the numbers before removing board from the list
        #TODO better understand what happens when you remove an item from the iterator 
        for board in boards:
            markNumber(board, number)
        for board in boards:
            winner = checkBoard(board, number)
            if winner:
                if len(boards) == 1:
                    return number, board
                boards.remove(board)
            
                
def calcAnswer(number, board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 'X':
                total += board[i][j]
    return total * number
    
with open('Data.txt') as data:
    numbers = [int(item) for item in data.readline().split(",")]
    data.readline() #blank line
    boards = getBoards(data)
    lastWinningNumber, lastWinningBoard  = playBingo(numbers, boards)
    print("Last Winning number:", lastWinningNumber)
    print("Last Winning board:", lastWinningBoard)
    print(calcAnswer(lastWinningNumber, lastWinningBoard))
     
            
        
    
        