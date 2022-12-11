from tqdm import tqdm

class Monkey:

    def __init__(self, monkeyID, heldItems, monkeyTest, monkeyOperation, ifTruePass, ifFalsePass, inspectCount):

        self.monkeyID = monkeyID
        self.heldItems = heldItems
        self.monkeyTest = monkeyTest
        self.monkeyOperation = monkeyOperation
        self.ifTruePass = ifTruePass
        self.ifFalsePass = ifFalsePass
        self.inspectCount = inspectCount


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
            listOfMonkeys.append(Monkey(monkeyNumber, itemsToSort, test, operation, monkeyToThrowIfTrue, monkeyToThrowIfFalse, 0))
      

    for monkee in listOfMonkeys:
        monkee.printInfo()

    print()
    print(f'Number of monkeys = {len(listOfMonkeys)}')
    input()

    for round in tqdm(range(1, 10001, 1)):

        #print(f'~~ ROUND {round} ~~')

        for monkee in listOfMonkeys:

            #print(f"MONKEY {monkee.monkeyID}")

            for item in monkee.heldItems:

                monkee.inspectCount += 1

                if (monkee.monkeyOperation.split(' ')[-2] == '*' and monkee.monkeyOperation.split(' ')[-1] == 'old'):
                    #print("hit the exponent monkey!")
                    item = item * item

                elif (monkee.monkeyOperation.split(' ')[-2] == '*'):
                    item = item * int(monkee.monkeyOperation.split(' ')[-1])

                elif (monkee.monkeyOperation.split(' ')[-2] == '+'):   
                    item = item + int(monkee.monkeyOperation.split(' ')[-1])


                #item = item // 3
                #print(item)

                if (item % int(monkee.monkeyTest.split(' ')[-1]) == 0):
                    #print("Divisable!!!")
                    #print(f'Throw to {monkee.ifTruePass}')
                    listOfMonkeys[monkee.ifTruePass].heldItems.append(item)

                elif (item % int(monkee.monkeyTest.split(' ')[-1]) != 0):
                    #print("Not Divisable!!!")
                    #print(f'Throw to {monkee.ifFalsePass}')
                    listOfMonkeys[monkee.ifFalsePass].heldItems.append(item)

            monkee.heldItems = []
    
        for monkee in listOfMonkeys:
            #print(f'Monkey {monkee.monkeyID}: {monkee.heldItems}')
            pass

    for monkee in listOfMonkeys:
        print(f'Monkey {monkee.monkeyID} inspected items {monkee.inspectCount} times.')  