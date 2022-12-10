class RopeSegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#This shouldve just been C++ lol

with open('input.txt', newline='') as csvfile:  

    content = csvfile.read().splitlines()

    head = RopeSegment(0,0)
    tail = RopeSegment(0,0)

    listOfAllTailCoordinates = []

    #print(f'current head location: ({head.x},{head.y})')
    #print(f'current tail location: ({tail.x},{tail.y})')

    for row in content:
        
        direction = row.split(' ')[0]
        distance = int(row.split(' ')[1])
        #print(f'Travel {distance} in {direction} direction')

        for distanceStepCounter in range(distance, 0, -1):
            
            #Take steps for the HEAD
            if direction == 'U':
                head.y += 1
            elif direction == 'D':
                head.y -= 1
            elif direction == 'R':
                head.x += 1
            elif direction == 'L':
                head.x -= 1

            #Oh my gosh isaac dont look at this

            if(abs(head.y - tail.y) == 1 and abs(head.x - tail.x) == 1):
                pass
                #print("Diagonal case, but chill")
            elif(head.y - tail.y == 2 and head.x - tail.x == -1):
                tail.y += 1
                tail.x -= 1
            elif(head.y - tail.y == 2 and head.x - tail.x == 1):
                tail.y += 1
                tail.x += 1
            elif(head.y - tail.y == -2 and head.x - tail.x == -1):
                tail.y -= 1
                tail.x -= 1
            elif(head.y - tail.y == -2 and head.x - tail.x == 1):
                tail.y -= 1
                tail.x += 1
            elif(head.y - tail.y == -1 and head.x - tail.x == 2):
                tail.y -= 1
                tail.x += 1
            elif(head.y - tail.y == 1 and head.x - tail.x == 2):
                tail.y += 1
                tail.x += 1
            elif(head.y - tail.y == -1 and head.x - tail.x == -2):
                tail.y -= 1
                tail.x -= 1
            elif(head.y - tail.y == 1 and head.x - tail.x == -2):
                tail.y += 1
                tail.x -= 1
            else:
                if(head.y - tail.y > 1):
                    tail.y += 1
                if(tail.y - head.y > 1):
                    tail.y -= 1
                if(head.x - tail.x > 1):
                    tail.x += 1
                if(tail.x - head.x > 1):
                    tail.x -= 1

            #print(f'current head location: ({head.x},{head.y})')
            #print(f'current tail location: ({tail.x},{tail.y})')


            if ([tail.x, tail.y] not in listOfAllTailCoordinates):
                listOfAllTailCoordinates.append([tail.x, tail.y])

    print(f'Total number of tail spots is {len(listOfAllTailCoordinates)}')

