class RopeSegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#This shouldve just been C++ lol

with open('input.txt', newline='') as csvfile:  

    content = csvfile.read().splitlines()

    head = RopeSegment(0,0)
    tail = RopeSegment(0,0)

    print(f'current head location: ({head.x},{head.y})')
    print(f'current tail location: ({tail.x},{tail.y})')

    for row in content:
        
        direction = row.split(' ')[0]
        distance = int(row.split(' ')[1])
        print(f'Travel {distance} in {direction} direction')

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

            #Check where to go for the TAIL

            if(abs(head.y - tail.y) == 1 and abs(head.x - tail.x) == 1):
                print("Diagonal case!!!")

                



                input()

            else:
                if(head.y - tail.y > 1):
                    tail.y += 1
                if(tail.y - head.y > 1):
                    tail.y -= 1
                if(head.x - tail.x > 1):
                    tail.x += 1
                if(tail.x - head.x > 1):
                    tail.x -= 1

            print(f'current head location: ({head.x},{head.y})')
            print(f'current tail location: ({tail.x},{tail.y})')
            print()
            #input()

