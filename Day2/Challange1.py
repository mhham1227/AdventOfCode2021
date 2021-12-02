horizontal = 0
depth = 0
with open('Data.txt') as data:
    directions = data.readlines()
    for direction in directions:
        if "forward" in direction:
            horizontal = horizontal + int(direction[-2])
        elif "up" in direction:
            depth = depth - int(direction[-2])
        elif "down" in direction:
            depth = depth + int(direction[-2])
        else:
            print("Direction not found")
print("Horizontal: " + str(horizontal))
print("Depth: " + str(depth))

           