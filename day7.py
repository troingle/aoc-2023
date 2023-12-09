import random

chars =  ['A', 'K', 'Q', 'J', 'T', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

with open('input.txt') as f:
    input = f.read().split("\n")


for i in range(len(input)):
    for j in range(0, len(input) - i - 1):
        power1 = 0
        charSpots = [0] * 36

        # which is greater?

        for c in input[j].split(" ")[0]:
            charSpots[chars.index(str(c))] += 1

        types = sum(1 for element in charSpots if element != 0) # fancy line of code I did not write
        
        if types == 1:
            power1 = 1000000 + (16 - chars.index(input[j][0])) # FIVE OF A KIND
        elif types == 2: # if there are 2 different card types
            # check the list max
            max = 0
            for i in charSpots:
                if i > max:
                    max = i

            x = 0 # the number of different cards
            for c in input[j].split(" ")[0]:
                if c != chars[charSpots[max]]:
                    x += 1
            if x == 1:
                power1 = 1000000 + (16 - chars.index(input[j][0])) # FOUR OF A KIND

        print(power1)
        

        if True: # if is greater: aka bubble sort activation
            temp = input[j]
            input[j] = input[j+1]
        input[j+1] = temp

#print(input)
