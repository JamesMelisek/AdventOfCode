
# nobody look at this handbombed code


with open('input.txt', newline='') as csvfile:
    
    content = csvfile.readlines()
    totalScore = 0
    roundScore = 0

    for row in content:

        opthrow = row[0]
        mythrow = row[2]

        if mythrow == 'X':
            roundScore = roundScore + 1
            if opthrow == 'A':
                roundScore = roundScore + 3
            elif opthrow == 'C':
                roundScore = roundScore + 6

        elif mythrow == 'Y':
            roundScore = roundScore + 2
            if opthrow == 'B':
                roundScore = roundScore + 3
            elif opthrow == 'A':
                roundScore = roundScore + 6

        elif mythrow == 'Z':
            roundScore = roundScore + 3
            if opthrow == 'C':
                roundScore = roundScore + 3
            elif opthrow == 'B':
                roundScore = roundScore + 6

        totalScore = totalScore + roundScore
        roundScore = 0

    print(totalScore)
