
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
    for dirs in list:
        print(f'{dirs.name}')
    print()



def printFS(listOfDirs):
    print('Total system:')

    for dirs in listOfDirs:

        print (f'{dirs.name},   {type(dirs)}, Parent:{dirs.parentDirectory.name}')

        for kid in dirs.children:
            print (f'----------{kid.name},   {type(kid)}')

        print()

    print()




def findDirectoryInListWithChild(directories, nameToFind, childWithin):
    
    for dir in directories:

        if dir.name == nameToFind and childWithin in dir.children:

            print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Found directory in list: {dir}')
            return dir

    print(f'------------------has children---------------- Did not find: {dir.name} with child {childWithin.name}')

def findDirectoryInListWithParent(directories, nameToFind, pDirectory):
    
    for dir in directories:

        if dir.name == nameToFind and dir.parentDirectory == pDirectory:

            print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Found directory in list: {dir}')
            return dir

    print(f'-----------------has parent------------------ Did not find: {nameToFind} with parent {pDirectory.name}')


def getChildFromDirectory(parent, nameToFind):

    for kid in parent.children:

        if kid.name == nameToFind:

            print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Found child in parent: {kid}')
            return kid

    print(f'-------------------pull child from direct------------- Did not find: {nameToFind} in parent {parent.name}')


with open('input.txt', newline='') as csvfile:  

    content = csvfile.read().splitlines() 

    nullParentDirectory = Directory("NULL",[])
    currentDirectory = nullParentDirectory

    listOfDirectories = []
    listOfDirectories.append(Directory("/", nullParentDirectory))
    printSavedDirectories(listOfDirectories)
    

    for row in content:  

        if (row[0:4] == "$ ls"):
            print(f'LS  : ' + row + '\n')



        elif (row[0:4] == "$ cd"):
            print(f'CD : ' + row)
            
            if(row[5:7] == ".."):
                print(f'MOVE TO PARENT: {row}')
                print(f'New directory: {currentDirectory.name}')
                currentDirectory = currentDirectory.parentDirectory
            else:
                print(f"MOVE TO DIR: {row.split(' ')[2]}")

                printSavedDirectories(listOfDirectories)
                print(currentDirectory.name)
                currentDirectory = getChildFromDirectory(currentDirectory, row.split(' ')[2])

                print(f'New directory: {currentDirectory.name}')
                print("SUCESS IN MOVING TO DIRECTORY")

            print()

        elif (row[0:3] == "dir"):
            print(f'DIR : ' + row)

            
            #check if it already exists before creating new
            if (findDirectoryInListWithParent(listOfDirectories, row.split(' ')[1], currentDirectory) == None):

                newDir = Directory(row.split(' ')[1], currentDirectory)
                print(f'>>>Dir name:{newDir.name}, parent Directory:{newDir.parentDirectory.name}')
                listOfDirectories.append(newDir)
                findDirectoryInListWithParent(listOfDirectories, currentDirectory.name, currentDirectory.parentDirectory).addChildren(newDir)
    
        else:
            print(f'FILE: ' + row)
            newFile = File(row.split(' ')[1], row.split(' ')[0], currentDirectory)
            print(f'>>>File name:{newFile.name}, fileSize:{newFile.fileSize}, parentDirect:{newFile.parentDirectory.name}')

            findDirectoryInListWithParent(listOfDirectories, currentDirectory.name, currentDirectory.parentDirectory).addChildren(newFile)



        printFS(listOfDirectories)
        #input()
    
    printFS(listOfDirectories)