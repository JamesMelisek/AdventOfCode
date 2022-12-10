def displayScreen(bigList):
    for i in range(0, 5, 1):
        for character in list(displayMatrix[i * 39 : 39 + (i * 39) ]):
            print(character,end='')
        print()


with open('input.txt', newline='') as csvfile:  

    content = csvfile.read().splitlines()


    registerX = 1
    cycleCounter = 0
    signalStrengthSum = 0

    displayMatrix = ['.' for x in range(6 * 40)] 
    displayScreen(displayMatrix)


    for row in content:
        
        if (row[0:4] == "noop"):     
            
            #print('NOOP COMMEND:' + row)
            cycleCounter += 1

            if(cycleCounter == 20 or cycleCounter == 60 or cycleCounter == 100 or cycleCounter == 140 or cycleCounter == 180 or cycleCounter == 220):
                print(f'CALCULATING {cycleCounter * registerX}')
                signalStrengthSum += (cycleCounter * registerX)


        elif (row[0:4] == "addx"):
            
            increment = int(row.split(' ')[1])

            cycleCounter += 1

            if(cycleCounter == 20 or cycleCounter == 60 or cycleCounter == 100 or cycleCounter == 140 or cycleCounter == 180 or cycleCounter == 220):
                print(f'CALCULATING {cycleCounter * registerX}')
                signalStrengthSum += (cycleCounter * registerX)

            cycleCounter += 1

            if(cycleCounter == 20 or cycleCounter == 60 or cycleCounter == 100 or cycleCounter == 140 or cycleCounter == 180 or cycleCounter == 220):
                print(f'CALCULATING {cycleCounter * registerX}')
                signalStrengthSum += (cycleCounter * registerX)

            registerX += increment

            print(f'ADDX COMMEND: {increment} , {row}')

        #print(f'after cycleCounter = {cycleCounter}, registerX = {registerX}')
        #input()


    print(f'The answer is {signalStrengthSum}')