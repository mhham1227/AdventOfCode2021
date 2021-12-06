def mapFishAges():
    #Number of fishes ready to hatch
    hatchFishes = fishAgesDict[0]
    #Shift fishes ages down by 1
    fishAgesDict[0], fishAgesDict[1], fishAgesDict[2], fishAgesDict[3], fishAgesDict[4], fishAgesDict[5], fishAgesDict[6], fishAgesDict[7] = fishAgesDict[1], fishAgesDict[2], fishAgesDict[3], fishAgesDict[4], fishAgesDict[5], fishAgesDict[6], fishAgesDict[7], fishAgesDict[8]
    #Reset the new mama's & papa's back to 6
    fishAgesDict[6] += hatchFishes
    #Set the new babies to 8
    fishAgesDict[8] = hatchFishes
    
with open('Data.txt') as data:
    days = 256
    fishAges = [int(item) for item in data.readline().split(",")]
    fishAgesDict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

    for fish in fishAges:
        fishAgesDict[fish] += 1
    print(fishAgesDict)

    for day in range(1, days + 1):
        mapFishAges()
        
print(fishAgesDict)
print(sum(fishAgesDict.values()))
        

            
