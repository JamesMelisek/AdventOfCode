import math

with open('input.txt', newline='') as csvfile:  

    content = csvfile.readlines()
    listOfStacks = [[] for _ in range(9)]

    for rowCounter, row in enumerate(content):
        
        if (rowCounter <= 7):

            for characterLoopCounter, character in enumerate(list(row[:-1])):

                if (characterLoopCounter - 1) % 4 == 0:
                    
                    if character != " ":
                        listOfStacks[math.floor(characterLoopCounter / 4)].append(character)
        
        elif(rowCounter > 9):

            instructions = row[:-1].split(' ')

            moveAmount = int(instructions[1])
            moveFrom = int(instructions[3])
            moveTo = int(instructions[5])

            for i in range(moveAmount):
                listOfStacks[moveTo - 1].insert(0, listOfStacks[moveFrom - 1].pop(0))

print([item[0] for item in listOfStacks])