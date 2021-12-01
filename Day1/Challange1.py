with open('Data.txt') as data:
    depth = data.readlines()
    
    count = 1
    for i in range(1,len(depth)):
        if depth[i] > depth[i-1]:
            count = count + 1
            print(str(depth[i]) + " (increased) count: " + str(count))
        else:
            print(str(depth[i]) + " (decreased) count: " + str(count))
    print(count)