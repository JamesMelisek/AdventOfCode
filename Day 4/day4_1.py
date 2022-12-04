
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

        leftOver = [x for x in elf1DutyList if x not in elf2DutyList]
        leftOver2= [x for x in elf2DutyList if x not in elf1DutyList]

        if not leftOver or not leftOver2:
            print("Nothing left in one or both of em")
            emptyAssignmentCounter += 1
        else:
            print(leftOver)
            print(leftOver2)


    print(emptyAssignmentCounter)

