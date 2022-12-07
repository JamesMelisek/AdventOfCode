
class File:
       
    def __init__(self, name, fileSize, parentDirectory):
        self.name = name
        self.fileSize = fileSize
        self.parentDirectory = parentDirectory


class Directory:
    
    def __init__(self, name, parentDirectory):

        self.name = name
        self.parentDirectory = parentDirectory
        self.children = []

    def addChildren(self, child):
        self.children.append(child)


def printSavedDirectories(list):
    print('List of all stored directories:')
    for dirs in list.children:
        print(f'{dirs.name}')
    print()



def printFS(direct):
    print('Total system:')

    for child in direct.children:
       
        if child is File:
            print(child.name)
        else:
            print(child.name)
        #else:
            printFS(child)


def getChildIndex(currentDirectory, targetDirectoryName):

    for idx, kid in enumerate(currentDirectory.children):

        if kid.name == targetDirectoryName:

            print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Found child in parent: {kid}')
            return idx

    print(f'-------------------get child index using name---------- Did not find: {targetDirectoryName} in parent {currentDirectory.name}')
    return 10000000000000




def findDirectoryInListWithChild(directories, nameToFind, childWithin):
    
    for dir in directories:

        if dir.name == nameToFind and childWithin in dir.children:

            print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Found directory in list: {dir}')
            return dir

    print(f'------------------has children---------------- Did not find: {dir.name} with child {childWithin.name}')
def findDirectoryInListWithParent(directories, nameToFind, pDirectory):
    
    for dir in directories:

        if dir.name == nameToFind and dir.parentDirectory.name == pDirectory:

            print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Found directory in list: {dir}')
            return dir

    print(f'-----------------has parent------------------ Did not find: {nameToFind} with parent {pDirectory.name}')
def getChildFromDirectory(parent, nameToFind):

    for kid in parent.children:

        if kid.name == nameToFind:

            print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Found child in parent: {kid}')
            return kid

    print(f'-------------------pull child from direct------------- Did not find: {nameToFind} in parent {parent.name}')


ultimateParentDirectory = 0

with open('input.txt', newline='') as csvfile:  

    content = csvfile.read().splitlines() 

    nullParentDirectory = Directory("NULL", [])
    nullParentDirectory.children.append(Directory('/',nullParentDirectory))

    ultimateParentDirectory = nullParentDirectory
    currentDirectory = nullParentDirectory
    

    for row in content:  

        if (row[0:4] == "$ ls"):
            print(f'LS  : ' + row + '\n')



        elif (row[0:4] == "$ cd"):
            print(f'CD : ' + row)
            
            if(row[5:7] == ".."): # CD ..

                print(f'MOVE TO PARENT: {row}')
                print(f'New directory: {currentDirectory.name}')

                currentDirectory = currentDirectory.parentDirectory

            else: # CD NAME

                targetDirectoryName = row.split(' ')[2]
                print(f"MOVE TO DIR: {targetDirectoryName}")

                #printSavedDirectories(listOfDirectories)
                print(currentDirectory.name)
                print(len(currentDirectory.children))

                printSavedDirectories(currentDirectory)
                currentDirectory = currentDirectory.children[getChildIndex(currentDirectory, targetDirectoryName)] # Get the child that is in dere already

                print(f'Moved into new directory: {currentDirectory.name}')
                print("SUCESS IN MOVING TO DIRECTORY")

            print()

        elif (row[0:3] == "dir"):
            print(f'DIR : ' + row)

            listedDirectoryName = row.split(' ')[1]

            #check if it already exists in directory
            if (currentDirectory.children):

                newDir = Directory(row.split(' ')[1], currentDirectory)
                print(f'>>>Dir name:{newDir.name}, parent Directory:{newDir.parentDirectory.name}')

                currentDirectory.addChildren(newDir)

                #findDirectoryInListWithParent(listOfDirectories, currentDirectory.name, currentDirectory.parentDirectory).addChildren(newDir)
    
        else:
            print(f'FILE: ' + row)

            newFile = File(row.split(' ')[1], row.split(' ')[0], currentDirectory)
            print(f'>>>File name:{newFile.name}, fileSize:{newFile.fileSize}, parentDirect:{newFile.parentDirectory.name}')

            currentDirectory.addChildren(newFile)


        printFS(currentDirectory)
        input()
    
   # printFS(listOfDirectories)