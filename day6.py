ways = 0

with open('input.txt') as f:
    input = f.read().split(" ")
    
times, distances = [int(input[8]), int(input[13]), int(input[18]), int(input[23].replace("\nDistance:", ""))], [int(input[26]), int(input[29]), int(input[32]), int(input[35])]

time, distance = "", ""

for n in range(len(times)):
    time = str(time) + str(times[n])
    distance = str(distance) + str(distances[n])

time, distance = int(time), int(distance)

for i in range(time):
    if (time - i) * i > distance:
        ways += 1

print(ways)

