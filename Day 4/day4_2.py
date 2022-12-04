
def getListOfDuties(lowerBound, higherBound):

    listOfJobs = []
    counter = int(lowerBound)

    while (counter <= int(higherBound)):

        listOfJobs.append(int(counter))
        counter += 1

    return listOfJobs




with open('input.txt', newline='') as csvfile:
    
    content = csvfile.readlines()

    emptyAssignmentCounter = 0

    for row in content:

        halfLists = str.split(row[:-1],",")

        leftRange = str.split(halfLists[0], "-")
        rightRange = str.split(halfLists[1], "-")


        elf1DutyList = getListOfDuties(leftRange[0],leftRange[1])
        elf2DutyList = getListOfDuties(rightRange[0],rightRange[1])

        print(row[:-1])
        print(elf1DutyList)
        print(elf2DutyList)


        overlappedDuties = any(elem in elf1DutyList for elem in elf2DutyList)
        print(overlappedDuties)

        if (overlappedDuties):
            emptyAssignmentCounter += 1

        #input()


    print(emptyAssignmentCounter)

