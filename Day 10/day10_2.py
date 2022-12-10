def displayScreen(bigList):
    for i in range(0, 6, 1):
        for character in list(displayMatrix[i * 40 : 40 + (i * 40) ]):
            print(character,end='')
        print()


with open('input.txt', newline='') as csvfile:  

    content = csvfile.read().splitlines()


    registerX = 1
    cycleCounter = 0

    spriteLocation = [0, 1 ,2]

    displayMatrix = ['.' for x in range(6 * 40)] 

    displayScreen(displayMatrix)


    for row in content:
        
        if (row[0:4] == "noop"):     
            
            if(cycleCounter % 40 == spriteLocation[0] or cycleCounter % 40 == spriteLocation[1] or cycleCounter % 40 == spriteLocation[2]):
                displayMatrix[cycleCounter] = '#'

            #step to next
            cycleCounter += 1


        elif (row[0:4] == "addx"):
            
            increment = int(row.split(' ')[1])

            if(cycleCounter % 40 == spriteLocation[0] or cycleCounter % 40 == spriteLocation[1] or cycleCounter % 40 == spriteLocation[2]):
                displayMatrix[cycleCounter] = '#'

            cycleCounter += 1
      

            if(cycleCounter % 40 == spriteLocation[0] or cycleCounter % 40 == spriteLocation[1] or cycleCounter % 40 == spriteLocation[2]):
                displayMatrix[cycleCounter] = '#'

            registerX += increment
            spriteLocation[0] = registerX - 1
            spriteLocation[1] = registerX
            spriteLocation[2] = registerX + 1

            cycleCounter += 1

        #print()
        #print(f'after cycleCounter = {cycleCounter}, spriteLocation = {spriteLocation}, regsiterx = {registerX}, last increment = {increment}')
        #displayScreen(displayMatrix)
        #print(displayMatrix)
        #input()


    displayScreen(displayMatrix)


    #print(f'The answer is {signalStrengthSum}')