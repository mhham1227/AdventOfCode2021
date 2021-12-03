gamma = ''
epsilon = ''

with open('Data.txt') as data:
    diagnostics = data.readlines()
    for i in range(0,len("000011101111")):
        one_counter = 0
        zero_counter = 0
        for power in diagnostics:
            print(power)
            if power[i] == '1':
                one_counter = one_counter + 1
            elif power[i] == '0':
                zero_counter = zero_counter + 1
            else:
                print("COULD NOT MATCH")
        
        if one_counter > zero_counter:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
print("GAMMA: " + gamma)
print("EPSILON: " + epsilon)          
        