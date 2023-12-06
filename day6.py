
sum = 1
allWays = []

with open('input.txt') as f:
    input = f.read().split(" ")
    
times, distances = [int(input[8]), int(input[13]), int(input[18]), int(input[23].replace("\nDistance:", ""))], [int(input[26]), int(input[29]), int(input[32]), int(input[35])]

#times, distances = [7, 15, 30], [9, 40, 200] # test input

print(times)
print(distances)

for i in range(len(times)): # for each race
    ways = 0
    for n in range(times[i]): # calculate how many possibilities, n being the time we hold the button for AND our speed
        if (times[i] - n) * n > distances[i]:
            ways += 1
    
    allWays.append(ways)

for w in allWays:
    sum *= w

print(sum)