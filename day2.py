sum = 0

with open('day2input.txt') as f:
    input = f.readlines()

for i in input: # for one set of three sets
    impossible = False
    redMax = 12
    greenMax = 13
    blueMax = 14

    reds = []
    blues = []
    greens = []

    id = i[5]
    try:
        id = id + str(int(i[6])) # checks if integer
    except:
        pass

    try:
        id = id + str(int(i[7]))
    except:
        pass

    
    sets = i.split(':')
    sets = sets[1].replace(" ", "").replace("\n", "").split(";")

    for n in sets: # for subset
        if "green" in n:
            green = n[n.find("green") - 1]
            try:
                green = str(int(n[n.find("green") - 2])) + str(green)
            except:
                pass
        else:
            green = 0

        if "blue" in n:
            blue = n[n.find("blue") - 1]
            try:
                blue = str(int(n[n.find("blue") - 2])) + str(blue)
            except:
                pass
        else:
            blue = 0

        if "red" in n:
            red = n[n.find("red") - 1]
            try:
                red = str(int(n[n.find("red") - 2])) + str(red)
            except:
                pass
        else:
            red = 0

        reds.append(int(red))
        blues.append(int(blue))
        greens.append(int(green))

        if int(red) > redMax or int(blue) > blueMax or int(green) > greenMax:
            impossible = True
    
    redMax = max(reds)
    blueMax = max(blues)
    greenMax = max(greens)

    sum += redMax * blueMax * greenMax


            


print(sum)

   

