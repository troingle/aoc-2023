sum = 0

# 28256 too high

with open('input.txt') as f:
    input = f.readlines()

for i in input: # for one row
    i = i.split(" | ")
    for j in i: # for set of 2 parts
        list = []
        matches = 0
        points = 0
        list.insert(0, i[1].replace("\n", "").replace(":", "").split(" "))
        i.remove(i[1])
        id = i[0].replace("\n", "").replace(":", "").split(" ")[1]
        list.insert(0, i[0].replace("\n", "").replace(":", "").split(" "))
        list[0] = list[0][2:]
        print("-- CARD " + id + " --")
        for k in list[1]: # for number
            if k == "":
                list[1].remove(k)
        for n in list[0]:
            if n in list[1]: # if match
                matches += 1
        print("matches: ", matches)
        if matches > 0:
            points = 1
            for m in range(1, matches):
                points *= 2
        print(points)
        sum += points
        print("sum after adding: ", sum)
    

print(sum)