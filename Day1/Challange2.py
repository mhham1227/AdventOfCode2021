subWindowSize =2 #0 based - real size = 3
count = 0
windowSum=0
prevSum = float('inf')
with open('Data.txt') as data:
    depth = data.readlines()
    for i in range(0,len(depth)):
        windowSum = windowSum + int(depth[i])
        if(i >= subWindowSize):
            if windowSum > prevSum:
                count = count + 1
            #print("Current Window: " + str(windowSum) + " Previous Window: " + str(prevSum) + " Count: " + str(count))
            prevSum = windowSum
            windowSum = windowSum - int(depth[i-subWindowSize])
    print("Count: " + str(count))
