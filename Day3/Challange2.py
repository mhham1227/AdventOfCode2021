def filterData(diagnostics, position, ratingName):
    newData = []
    zero_counter, one_counter = getPositionValues(diagnostics)
    if(ratingName == "oxygen"):
        value = mostCommon(zero_counter, one_counter)
    elif(ratingName =="co2Scubber"):
        value = leastCommon(zero_counter, one_counter)
        
    for data in diagnostics:
        if data[position] == value:
            newData.append(data)
    return newData
def leastCommon(zero_counter, one_counter):
    if one_counter < zero_counter:
        return '1'
    if zero_counter <= one_counter:
        return '0'
def mostCommon(zero_counter, one_counter):
    if one_counter >= zero_counter:
        return '1'
    if zero_counter > one_counter:
        return '0'
def getPositionValues(diagnostics):
    one_counter = 0
    zero_counter = 0
    for power in diagnostics:
            if power[i] == '1':
                one_counter = one_counter + 1
            elif power[i] == '0':
                zero_counter = zero_counter + 1
            else:
                print("COULD NOT MATCH")
    return zero_counter, one_counter

with open('Data.txt') as data:
    oxygenData = data.readlines()
    co2ScrubberData = oxygenData.copy()
    for i in range(0,len("000011101111")):
        oxygenData = filterData(oxygenData, i, "oxygen")
        co2ScrubberData = filterData(co2ScrubberData, i, "co2Scubber")
        if len(oxygenData) == 1:
            print("ANSWER Oxygen: " + oxygenData[0])
        if len(co2ScrubberData) == 1:
            print("ANSWER CO2: " + co2ScrubberData[0])
                    