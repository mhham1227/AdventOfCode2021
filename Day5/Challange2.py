ventLocation= {}
def getCords(vent):
    cords = vent.split("->")
    start = [int(x) for x in cords[0].split(",")] 
    end = [int(x) for x in cords[1].split(",")]
    return (start[0], start[1]), (end[0], end[1])
def addVentLoc(start, end):
    reverseX = -1 if start[0] > end[0] else 1
    reverseY = -1 if start[1] > end[1] else 1
    if start[0] == end[0]:
        for y in range(start[1], end[1]+reverseY, reverseY):
            ventLocation[(start[0],y)] = ventLocation.get((start[0], y)) + 1 if ventLocation.get((start[0],y)) != None else 1
    elif start[1] == end[1]:
        for x in range(start[0], end[0]+reverseX, reverseX):
            ventLocation[(x,start[1])] = ventLocation.get((x, start[1])) + 1 if ventLocation.get((x, start[1])) != None else 1
    else:
        for x, y in zip(range(start[0], end[0]+reverseX, reverseX), range(start[1], end[1]+reverseY, reverseY)):
            ventLocation[(x,y)] = ventLocation.get((x, y)) + 1 if ventLocation.get((x, y)) != None else 1
    
with open('Data.txt') as data:
    vents = data.readlines()
    for vent in vents:
        cords = getCords(vent)
        addVentLoc(cords[0], cords[1])
    print(len({k:v for (k,v) in ventLocation.items() if v >= 2}))