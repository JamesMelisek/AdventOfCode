class RopeSegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def getMovement(parent, unmovedChild):

    child = unmovedChild

    if(abs(parent.y - child.y) == 1 and abs(parent.x - child.x) == 1):
        pass
    elif(parent.y - child.y == 2 and parent.x - child.x == -1):
        child.y += 1
        child.x -= 1
    elif(parent.y - child.y == 2 and parent.x - child.x == 1):
        child.y += 1
        child.x += 1
    elif(parent.y - child.y == -2 and parent.x - child.x == -1):
        child.y -= 1
        child.x -= 1
    elif(parent.y - child.y == -2 and parent.x - child.x == 1):
        child.y -= 1
        child.x += 1
    elif(parent.y - child.y == -1 and parent.x - child.x == 2):
        child.y -= 1
        child.x += 1
    elif(parent.y - child.y == 1 and parent.x - child.x == 2):
        child.y += 1
        child.x += 1
    elif(parent.y - child.y == -1 and parent.x - child.x == -2):
        child.y -= 1
        child.x -= 1
    elif(parent.y - child.y == 1 and parent.x - child.x == -2):
        child.y += 1
        child.x -= 1
    else:
        if(parent.y - child.y > 1):
            child.y += 1
        if(child.y - parent.y > 1):
            child.y -= 1
        if(parent.x - child.x > 1):
            child.x += 1
        if(child.x - parent.x > 1):
            child.x -= 1
            
    return child

with open('input.txt', newline='') as csvfile:  

    content = csvfile.read().splitlines()

    head = RopeSegment(0,0)
    tailSegmentArray = [RopeSegment(0,0) for i in range(9)]

    listOfAllTailCoordinates = []

    for row in content:
        
        direction = row.split(' ')[0]
        distance = int(row.split(' ')[1])

        for distanceStepCounter in range(distance, 0, -1):
            
            if direction == 'U':
                head.y += 1
            elif direction == 'D':
                head.y -= 1
            elif direction == 'R':
                head.x += 1
            elif direction == 'L':
                head.x -= 1
  
            for segIdx, segment in enumerate(tailSegmentArray):

                if(segIdx == 0):
                    segment = getMovement(head, segment)
                else:
                    segment = getMovement(tailSegmentArray[segIdx - 1], segment)
   
            if ([tailSegmentArray[8].x, tailSegmentArray[8].y] not in listOfAllTailCoordinates):
                listOfAllTailCoordinates.append([tailSegmentArray[8].x, tailSegmentArray[8].y])

    print(f'Total number of tail spots is {len(listOfAllTailCoordinates)}')