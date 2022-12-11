class Monkey:

    def __init__(self, monkeyID, heldItems, monkeyTest, monkeyOperation, ifTruePass, ifFalsePass):

        self.monkeyID = monkeyID
        self.heldItems = heldItems
        self.monkeyTest = monkeyTest
        self.monkeyOperation = monkeyOperation
        self.ifTruePass = ifTruePass
        self.ifFalsePass = ifFalsePass


    def printInfo(self):

        print()
        print(f'~~~~ MONKEE #{self.monkeyID} ~~~~')
        print(self.heldItems)
        print(self.monkeyTest)
        print(self.monkeyOperation)
        print(self.ifTruePass)
        print(self.ifFalsePass)


with open('test.txt', newline='') as csvfile:  

    content = csvfile.read().splitlines()

    monkeyNumber = -1
    itemsToSort = []
    operation = ''
    test  =''
    monkeyToThrowIfTrue = -1
    monkeyToThrowIfFalse = -1

    listOfMonkeys = []

    #Populate the monkeys
    for rowIdx, row in enumerate(content):
        
        if (rowIdx % 7 == 0):     
            monkeyNumber = row.split(' ')[1][:-1]

        elif (rowIdx % 7 == 1):
            itemsToSort =  row.split(':')[1].split(',')

            for idx, item in enumerate(itemsToSort):
                itemsToSort[idx] = int(item[1:])

        elif (rowIdx % 7 == 2):
            operation = row.split(':')[1][1:]

        elif (rowIdx % 7 == 3):
            test = row.split(':')[1][1:]
        
        elif (rowIdx % 7 == 4):
            monkeyToThrowIfTrue = int(row.split(' ')[-1])

        elif (rowIdx % 7 == 5):
            monkeyToThrowIfFalse = int(row.split(' ')[-1])

        elif (rowIdx % 7 == 6):
            listOfMonkeys.append(Monkey(monkeyNumber, itemsToSort, test, operation, monkeyToThrowIfTrue, monkeyToThrowIfFalse))
      
    #for monkee in listOfMonkeys:
    #    monkee.printInfo()

    for round in range(1):


        for monkee in listOfMonkeys:

            print(f"MONKEY {monkee.monkeyID}")

            for item in monkee.heldItems:

                testValue = 0

                if (monkee.monkeyOperation.split(' ')[-2] == '*' and monkee.monkeyOperation.split(' ')[-1] == 'old'):
                    print("hit the exponent monkey!")
                    testValue = item * item

                elif (monkee.monkeyOperation.split(' ')[-2] == '*'):
                    testValue = item * int(monkee.monkeyOperation.split(' ')[-1])

                elif (monkee.monkeyOperation.split(' ')[-2] == '+'):   
                    testValue = item + int(monkee.monkeyOperation.split(' ')[-1])


                testValue = testValue // 3
                print(testValue)

                if (testValue % int(monkee.monkeyTest.split(' ')[-1]) == 0):
                    print("Divisable!!!")
                    print(f'Throw to {monkeyToThrowIfTrue}, but located at index {monkeyToThrowIfTrue - 1 }')
                    listOfMonkeys[monkeyToThrowIfTrue - 1].heldItems.append(item)

                elif (testValue % int(monkee.monkeyTest.split(' ')[-1]) != 0):
                    print("Not Divisable!!!")
                    print(f'Throw to {monkeyToThrowIfFalse}, but located at index {monkeyToThrowIfFalse - 1 }')
                    listOfMonkeys[monkeyToThrowIfFalse - 1].heldItems.append(item)

       
                input()

    #print(f'The answer is {0}')