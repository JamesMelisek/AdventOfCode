with open('input.txt', newline='') as csvfile:  

    latestFour = []
    counter = 0

    for lines in csvfile:       
        for character in lines:

            counter += 1

            latestFour.append(character)

            if counter > 14:
                latestFour.pop(0)

            if (not any(latestFour.count(x) > 1 for x in latestFour) and counter > 14):                
                print(f'Hit one of the message things at {counter}!')
                break