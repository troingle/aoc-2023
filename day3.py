sum = 0
gearRatioSum = 0

symbols = ["*", "@", "#", "/", "=", "$", "+", "-", "&", "%"]

engine = []
usedNums = []

def checkNeighboringNumbers(i, j, engine, blacklist):
    num = engine[i][j]
    if engine[i][j + 1].isdigit():
        num = str(num) + engine[i][j + 1]
        if engine[i][j + 2].isdigit():
            num = num + engine[i][j + 2]

    if engine[i][j - 1].isdigit():
        num = engine[i][j - 1] + str(num)
        if engine[i][j - 2].isdigit():
            num = engine[i][j - 2] + num

    identifier = num + "-" + str(i)

    print(blacklist)
    print(identifier)

    if identifier in blacklist:
        print(num + " in blacklist")
        return 0
    else:
        blacklist.append(identifier)
        return int(num)
    
with open('input.txt') as f:
    input = f.read().split("\n")


for p in input:
    row = [*p]
    engine.append(row)


for i in range(len(engine)):
    for j in range(len(engine)):
        if engine[i][j] in symbols:
            try:
                blacklist = []
                identifier = []
                usedNums = []
                
                if engine[i][j - 1].isdigit():
                    num = checkNeighboringNumbers(i, j - 1, engine, blacklist)
                    usedNums.append(num)
                    sum += num
                if engine[i][j + 1].isdigit():
                    num = checkNeighboringNumbers(i, j + 1, engine, blacklist)
                    usedNums.append(num)
                    sum += num
                if engine[i - 1][j + 1].isdigit():
                    num = checkNeighboringNumbers(i - 1, j + 1, engine, blacklist)
                    usedNums.append(num)
                    sum += num
                if engine[i - 1][j - 1].isdigit():
                    num = checkNeighboringNumbers(i - 1, j - 1, engine, blacklist)
                    usedNums.append(num)
                    sum += num
                if engine[i - 1][j].isdigit():
                    num = checkNeighboringNumbers(i - 1, j, engine, blacklist)
                    usedNums.append(num)
                    sum += num
                if engine[i + 1][j - 1].isdigit():
                    num = checkNeighboringNumbers(i + 1, j - 1, engine, blacklist)
                    usedNums.append(num)
                    sum += num
                if engine[i + 1][j + 1].isdigit():
                    num = checkNeighboringNumbers(i + 1, j + 1, engine, blacklist)
                    usedNums.append(num)
                    sum += num
                if engine[i + 1][j].isdigit():
                    num = checkNeighboringNumbers(i + 1, j, engine, blacklist)
                    usedNums.append(num)
                    sum += num
                for n in usedNums:
                    if n == 0:
                        usedNums.remove(n)

                if len(usedNums) == 2:
                    ratio = usedNums[0] * usedNums[1]
                else:
                    ratio = 0

                if engine[i][j] == "*":
                    print("It's made up of " + str(usedNums) + ". Ratio sum: " +  str(gearRatioSum) + ", ratio to be added is " + str(ratio))
                    gearRatioSum += ratio

            except:
                pass


print(gearRatioSum)





