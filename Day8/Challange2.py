def getValueByLen(numberList, length):
    for i in range(0,len(numberList)+1):
        if len(numberList[i]) == length:
            return numberList[i]

def compareLettersOfSegment(sevenSegment, number, segmentNumber):
    return [letter in number for letter in sevenSegment[segmentNumber]]

def isTwo(sevenSegment, two):
    if len(two) != 5:
        return False
        
    rightSideFull = all(compareLettersOfSegment(sevenSegment, two, 0))
    topLeft = all(compareLettersOfSegment(sevenSegment, two, 5))
    
    if rightSideFull:
        return False
        
    if not topLeft:
        return True
def isThree(sevenSegment, three):
    if len(three) != 5:
        return False
    rightSideFull = all(compareLettersOfSegment(sevenSegment, three, 0))
    topLeft = all(compareLettersOfSegment(sevenSegment, three, 5))
    bottomLeft = all(compareLettersOfSegment(sevenSegment, three, 3))

    if rightSideFull and not topLeft and not bottomLeft:
        return True
        
def isFive(sevenSegment, five):
    if len(five) != 5:
        return False
        
    rightSideFull = all(compareLettersOfSegment(sevenSegment, five, 0))
    bottomLeft = all(compareLettersOfSegment(sevenSegment, five, 3))
    
    if rightSideFull:
        return False
        
    if not bottomLeft:
        return True
  
def isZero(sevenSegment, zero):
    if len(zero) != 6:
        return False
    middle = all(compareLettersOfSegment(sevenSegment, zero, 5))
    if not middle:
        return True
   
def isSix(sevenSegment, six):
    if len(six) != 6:
        return False
    topRight = all(compareLettersOfSegment(sevenSegment, six, 0))
    if not topRight:
        return True
        
def isNine(sevenSegment, nine):
    if len(nine) != 6:
        return False
    bottomLeft = all(compareLettersOfSegment(sevenSegment, nine, 3))
    if not bottomLeft:
        return True
        
def findMissingIdx(sevenSegment, number):

    for letter in number:
        for space in sevenSegment:
            return None
def getDisplayWireConfigs(numberList):
    displayLayout = [None] * 10
    displayLayout[1] = getValueByLen(numberList, 2)
    displayLayout[4] = getValueByLen(numberList, 4)
    displayLayout[7] = getValueByLen(numberList, 3)
    displayLayout[8] = getValueByLen(numberList, 7)
    for number in numberList:
            if number == "|":
                break
            if isZero(sevenSegment, number):
                displayLayout[0] = number
                #print("Zero: ",number)
            if isTwo(sevenSegment, number):
                displayLayout[2] = number
                #print("TWO: ",number)
            if isThree(sevenSegment, number):
                displayLayout[3] = number
                #print("Three: ",number)
            if isFive(sevenSegment, number):
                displayLayout[5] = number
                #print("Five: ",number)
            if isSix(sevenSegment, number):
                displayLayout[6] = number
                #print("Six: ",number)
            if isNine(sevenSegment, number):
                displayLayout[9] = number
                #print("Nine: ",number)
    return [''.join(sorted(number))for number in displayLayout]
    
def buildSevenSegment(numberList):
    sevenSegment = [None] * 7
    one = list(getValueByLen(numberList, 2))
  
    four = list(getValueByLen(numberList, 4))
    four = list(filter(lambda x: x not in one, four))

    seven = list(getValueByLen(numberList, 3))
    seven = list(filter(lambda x: x not in one, seven))
    
    eight = list(getValueByLen(numberList, 7))
    eight = list(filter(lambda x: x not in one + four + seven, eight))
   
    sevenSegment[0] = one
    sevenSegment[1] = one
    sevenSegment[2] = eight
    sevenSegment[3] = eight
    sevenSegment[4] = four
    sevenSegment[5] = four
    sevenSegment[6] = seven
    
    return sevenSegment

def getLineOutput(wireConfig, numberList):
    output = ''
    for i in range(-4, 0):
        sortedNumber = ''.join(sorted(numberList[i]))
        if sortedNumber in wireConfig:
            output += str(wireConfig.index(sortedNumber))
    return output
with open('Data.txt') as data:
    total = 0
    numbers = data.readlines()
    count = 0
    for numberline in numbers:
        numberList = numberline.strip().split(" ")
        sevenSegment = buildSevenSegment(numberList)
        wireConfig = getDisplayWireConfigs(numberList)
    
        total += int(getLineOutput(wireConfig, numberList))
        
    print(total)
                
        