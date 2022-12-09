
#This shouldve just been C++ lol

with open('input.txt', newline='') as csvfile:  

    content = csvfile.read().splitlines()

    Matrix = [[0 for x in range(99)] for y in range(99)] 
    scenicScoreMatrix = [[0 for x in range(99)] for y in range(99)] 

    for heightCounter, row in enumerate(content):
        for widthCounter, character in enumerate(list(row)):
            Matrix[heightCounter][widthCounter] = int(character)

    for rowIdx, row in enumerate(Matrix):
        for colIdx, column in enumerate(row):

            visibleNorth = 0
            visibleSouth = 0
            visibleEast = 0
            visibleWest = 0

            for i in range(rowIdx, 0, -1):        
                visibleNorth += 1           
                if (Matrix[i-1][colIdx] >= Matrix[rowIdx][colIdx]):
                    break

            for i in range(rowIdx, 98, 1):
                visibleSouth += 1
                if (Matrix[i+1][colIdx] >= Matrix[rowIdx][colIdx]):
                    break

            for i in range(colIdx, 0, -1):
                visibleWest += 1            
                if (Matrix[rowIdx][i-1] >= Matrix[rowIdx][colIdx]):
                    break

            for i in range(colIdx, 98, 1):
                visibleEast += 1            
                if (Matrix[rowIdx][i+1] >= Matrix[rowIdx][colIdx]):
                    break

            scenicScoreMatrix[rowIdx][colIdx] = visibleNorth * visibleSouth * visibleWest * visibleEast

    largestScore = 0

    for rowIdx, row in enumerate(scenicScoreMatrix):
        for colIdx, col in enumerate(row):
            if scenicScoreMatrix[rowIdx][colIdx] > largestScore:
                largestScore = scenicScoreMatrix[rowIdx][colIdx]

    print(f'The largest scenic score of any tree is {largestScore}')