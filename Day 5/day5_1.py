import math

with open('input.txt', newline='') as csvfile:  

    content = csvfile.readlines()
    listOfStacks = [[] for _ in range(9)]

    for rowCounter, row in enumerate(content):
        
        if (rowCounter <= 7):

            for characterLoopCounter, character in enumerate(list(row[:-1])):

                if (characterLoopCounter - 1) % 4 == 0:
                    
                    if character == " ":
                        print("_", end='')
                    else:
                        listOfStacks[math.floor(characterLoopCounter / 4)].append(character)

                        print(character, end='')
                        #print(listOfStacks)
                        #input()
            print()

        
        elif(rowCounter == 8):
            #print(listOfStacks)
            pass


        elif(rowCounter > 9):

            instructions = row[:-1].split(' ')

            moveAmount = int(instructions[1])
            moveFrom = int(instructions[3])
            moveTo = int(instructions[5])

            #print(f'{moveAmount}, {moveFrom}, {moveTo}')

            for i in range(moveAmount):

                #print(listOfStacks[moveTo - 1])
                #print(listOfStacks[moveFrom - 1])

            
                listOfStacks[moveTo - 1].insert(0, listOfStacks[moveFrom - 1].pop(0))


                #print(listOfStacks[moveTo - 1])
                #print(listOfStacks[moveFrom - 1])

print([item[0] for item in list])