with open('Data.txt') as data:
    fishAges = [int(item) for item in data.readline().split(",")]
    print("Init state: " , len(fishAges))
    for day in range(1, 81):
        daylyFishCount = len(fishAges)
        for fish in range(0, daylyFishCount):
            if fishAges[fish] != 0:
                fishAges[fish] -= 1
            elif fishAges[fish] == 0:
                fishAges[fish] = 6
                fishAges.append(8)
        print("After", day, "day: " , len(fishAges))

            
