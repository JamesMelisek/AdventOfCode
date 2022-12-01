f = open('input.txt', 'r')
content = f.readlines()
f.close()
largestThing = []
tempStore = 0
for row in content:
    if row == "\n":
        largestThing.append(tempStore)
        tempStore = 0
    else:
        tempStore = tempStore + int(row)
largestThing.sort()
print(largestThing[-1] + largestThing[-2] + largestThing[-3])