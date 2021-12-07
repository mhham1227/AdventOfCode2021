with open('Data.txt') as data:
    days = 256
    crabPositions = [int(item) for item in data.readline().split(",")]
    crabPositionsDict = {}

    for crab in crabPositions:
        crabPositionsDict[crab] = crabPositionsDict.get(crab) + 1 if crabPositionsDict.get(crab) else 1
    #print(crabPositionsDict)

    minFuel = float('inf')
    right = max(crabPositionsDict.keys())
    left = min(crabPositionsDict.keys())
    
    print(left, right)
    for pos in range(left, right):
        fuel = 0
        for key, value in crabPositionsDict.items():
            fuel += sum(range(0,abs(key-pos) + 1)) * value
        if fuel <= minFuel:
            minFuel = fuel

    print(minFuel)        
