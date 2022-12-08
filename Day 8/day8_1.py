with open('input.txt', newline='') as csvfile:  

    content = csvfile.read().splitlines()

    w, h = 99, 99
    Matrix = [[0 for x in range(w)] for y in range(h)] 

    for heightCounter, row in enumerate(content):
        for widthCounter, character in enumerate(list(row)):

            Matrix[heightCounter][widthCounter] = int(character)
            print(character, end='')

        print()
        #print(f' End of the road bucko {heightCounter}')

    for row in Matrix:
        for column in row:
            print(column, end='')
        print()


    totalTreesVisible = 0

    for rowIdx, row in enumerate(Matrix):
        for colIdx, column in enumerate(row):

            #Check if on the edge
            if (rowIdx == 0 or colIdx == 0 or rowIdx == 98 or colIdx == 98):
                totalTreesVisible += 1
                continue

            visibleNorth = True
            visibleSouth = True
            visibleEast = True
            visibleWest = True

            #check if anything N
            for i in range(rowIdx, 0, -1):
                #print(f'Current tree is: {Matrix[rowIdx][colIdx]} @({rowIdx},{colIdx}), comparing to: {Matrix[i-1][colIdx]}')             
                if (Matrix[i-1][colIdx] >= Matrix[rowIdx][colIdx]):
                    visibleNorth = False
                    
            #check if anything S
            for i in range(rowIdx, 98, 1):
                #print(f'Current tree is: {Matrix[rowIdx][colIdx]} @({rowIdx},{colIdx}), comparing to: {Matrix[i+1][colIdx]}')             
                if (Matrix[i+1][colIdx] >= Matrix[rowIdx][colIdx]):
                    visibleSouth = False

            #check if anything W
            for i in range(colIdx, 0, -1):
                #print(f'Current tree is: {Matrix[rowIdx][colIdx]} @({rowIdx},{colIdx}), comparing to: {Matrix[rowIdx][i-1]}')             
                if (Matrix[rowIdx][i-1] >= Matrix[rowIdx][colIdx]):
                    visibleWest = False

            #check if anything E
            for i in range(colIdx, 98, 1):
                #print(f'Current tree is: {Matrix[rowIdx][colIdx]} @({rowIdx},{colIdx}), comparing to: {Matrix[rowIdx][i+1]}')             
                if (Matrix[rowIdx][i+1] >= Matrix[rowIdx][colIdx]):
                    visibleEast = False

            #print(f'{Matrix[rowIdx][colIdx]}@({rowIdx},{colIdx})  north: {visibleNorth}, south: {visibleSouth}, west: {visibleWest}, east: {visibleEast}')
            if(visibleNorth or visibleSouth or visibleWest or visibleEast):
                totalTreesVisible += 1

    print(f'There are {totalTreesVisible} trees visible from the outside')