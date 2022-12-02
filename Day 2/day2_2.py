
# nobody look at this handbombed code


with open('input.txt', newline='') as csvfile:
    
    content = csvfile.readlines()
    totalScore = 0
    roundScore = 0

    for row in content:

        opthrow = row[0]
        outcome = row[2]

        if (outcome == 'X'):
            if (opthrow == 'A'):
                mythrow = 'Z'
            elif (opthrow == 'B'):
                mythrow = 'X'
            elif (opthrow == 'C'):
                mythrow = 'Y'

        elif (outcome == 'Y'):
            if (opthrow == 'A'):
                mythrow = 'X'
            elif (opthrow == 'B'):
                mythrow = 'Y'
            elif (opthrow == 'C'):
                mythrow = 'Z'

        elif (outcome == 'Z'):
            if (opthrow == 'A'):
                mythrow = 'Y'
            elif (opthrow == 'B'):
                mythrow = 'Z'
            elif (opthrow == 'C'):
                mythrow = 'X'

        if mythrow == 'X':
            roundScore += 1
            if opthrow == 'A':
                roundScore += 3
            elif opthrow == 'C':
                roundScore += 6

        elif mythrow == 'Y':
            roundScore = roundScore + 2
            if opthrow == 'B':
                roundScore += 3
            elif opthrow == 'A':
                roundScore += 6

        elif mythrow == 'Z':
            roundScore += 3
            if opthrow == 'C':
                roundScore += 3
            elif opthrow == 'B':
                roundScore += 6

        totalScore = totalScore + roundScore
        roundScore = 0

    print(totalScore)
