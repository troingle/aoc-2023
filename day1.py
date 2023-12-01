sum = 0
numNames = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] # twone oneight

with open('day1input.txt') as f:
    input = f.readlines()

for g in input:
    g = g.replace("\n", "")

for i in input: # for one word
    nums = []

    # works only for my specific list
    i = i.replace("oneight", "18")
    i = i.replace("twone", "21")
    i = i.replace("eightwo", "82")

    for x in numNames:
        if x in i:
            i = i.replace(x, str(numNames.index(x) + 1))

    for n in i: # for one character
        try:
            nums.append(int(n))
        except:
            pass
    num = str(nums[0]) + str(nums[-1])

    print(i, "=", num)

    sum += int(num)

print(sum)