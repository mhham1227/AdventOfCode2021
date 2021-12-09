with open('Data.txt') as data:
    numbers = data.readlines()
    count = 0
    for numberline in numbers:
        numberList = numberline.strip().split(" ")
        for i in range(-4, 0):
            if len(numberList[i]) in [2, 4, 3,7]:
                count += 1
                #print(numberList[i])
    print(count)