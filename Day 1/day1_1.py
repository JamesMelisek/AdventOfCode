
f = open('input.txt', 'r')
content = f.readlines()
f.close()

largestThing = 0
tempStore = 0

for row in content:

    if row == "\n":
        
        if (tempStore > largestThing):
            largestThing = tempStore

        tempStore = 0
        print("newline!!!")
        print("largest thing is")
    else:
        print(row,end="")
        tempStore = tempStore + int(row)

print(largestThing)