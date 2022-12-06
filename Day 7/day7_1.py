with open('input.txt', newline='') as csvfile:  

    latestFour = []
    counter = 0

    for lines in csvfile:       
        for character in lines:

            counter += 1

            latestFour.append(character)

            if counter > 4:
                latestFour.pop(0)


            print(f'Counter #: {counter} , latest 4: {latestFour}')

            if (not any(latestFour.count(x) > 1 for x in latestFour) and counter > 4):
                print(f'Hit one of the bit things at {counter}!')
                break