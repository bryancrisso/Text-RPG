import random
from colorama import Back, Style
def boolToConnection(value):
    if value:
        return '-'
    else:
        return ' '
class Room(object):
    content = 'n' # what is in the room ('n' for null, 'e' for empty)
    connections = [False,False,False,False] # NESW connections
    enemy = None
    traderType = None
    explored = False
    loot = []
    def __str__(self):
        return boolToConnection(self.connections[3]) + self.content + boolToConnection(self.connections[1])
class Generator(object):
    rooms = []
    def generate(self, mapSize, roomCount):
        currentRoomCount = 0
        array = [[Room() for y in range(mapSize[0])] for x in range(mapSize[1])]
        if roomCount > (mapSize[0]*mapSize[1]): #check if the amount of rooms can fit inside the floor
            print("Cannot fit the number of rooms within the floor!")
            return array
        while currentRoomCount < roomCount: #check if we have exceeded room limit
            for i in array:
                for j in i:
                    if not (currentRoomCount >= roomCount):
                        adjacentTesting = ['n', 'e', 's', 'w'] #NESW for eliminating directions when not surrounded by space
                        found = False

                        if j.content == 'n': #check if the current room has already been generated
                            if array.index(i) == 0 and i.index(j) == 0: #create the first room
                                j.content = 'e'
                                currentRoomCount += 1
                            else:
                                if i.index(j) != 0 and array.index(i) != 0 and array[array.index(i)] != array[-1] and i[i.index(j)] != i[-1]: #check if the room is surrounded by space or rooms
                                    if array[array.index(i)][i.index(j)-1].content != 'n' or array[array.index(i)-1][i.index(j)].content != 'n' or array[array.index(i)][i.index(j)+1].content != 'n' or array[array.index(i)+1][i.index(j)].content != 'n': #check to see if it is connected to any rooms
                                        if random.choice((True, False)):
                                            j.content = 'e'
                                            currentRoomCount += 1
                                else: #if the room is not surrounded by space we need to eliminate directions to test in
                                    if array.index(i) == 0:
                                        adjacentTesting.remove('n')
                                    if i.index(j) == 0:
                                        adjacentTesting.remove('w')
                                    if array[array.index(i)] == array[-1]:
                                        adjacentTesting.remove('s')
                                    if i[i.index(j)] == i[-1]:
                                        adjacentTesting.remove('e')

                                    #here we test in the directions confirmed
                                    if 'n' in adjacentTesting:
                                        if array[array.index(i)-1][i.index(j)].content != 'n' and random.choice((True, False)) and not found:
                                            j.content = 'e'
                                            found = True
                                            currentRoomCount += 1
                                    if 'e' in adjacentTesting:
                                        if array[array.index(i)][i.index(j)+1].content != 'n' and random.choice((True, False)) and not found:
                                            j.content = 'e'
                                            found = True
                                            currentRoomCount += 1
                                    if 's' in adjacentTesting:
                                        if array[array.index(i)+1][i.index(j)].content != 'n' and random.choice((True, False)) and not found:
                                            j.content = 'e'
                                            found = True
                                            currentRoomCount += 1
                                    if 'w' in adjacentTesting:
                                        if array[array.index(i)][i.index(j)-1].content != 'n' and random.choice((True, False)) and not found:
                                            j.content = 'e'
                                            found = True
                                            currentRoomCount += 1
        return array
    def createConnections(self, array):
        for i in array:
            for j in i:
                if j.content == 'e':
                    connections = [False, False, False, False]
                    adjacentTesting = ['n', 'e', 's', 'w'] #NESW for eliminating directions when not surrounded by space
                    if array.index(i) == 0:
                        adjacentTesting.remove('n')
                    if i.index(j) == 0:
                        adjacentTesting.remove('w')
                    if array[array.index(i)] == array[-1]:
                        adjacentTesting.remove('s')
                    if i[i.index(j)] == i[-1]:
                        adjacentTesting.remove('e')

                    #here we test in the directions confirmed
                    if 'n' in adjacentTesting:
                        if array[array.index(i)-1][i.index(j)].content == 'e':
                            connections[0] = True
                    if 'e' in adjacentTesting:
                        if array[array.index(i)][i.index(j)+1].content == 'e':
                            connections[1] = True
                    if 's' in adjacentTesting:
                        if array[array.index(i)+1][i.index(j)].content == 'e':
                            connections[2] = True
                    if 'w' in adjacentTesting:
                        if array[array.index(i)][i.index(j)-1].content == 'e':
                            connections[3] = True
                    j.connections = connections
        return array
    def displayMap(self, mapList, playerPos = [-1, -1]):
        for i in mapList:
            for j in i:
                if j.content != 'n':
                    if j.explored:
                        print(Back.GREEN, end='')
                    else:
                        print(Back.YELLOW, end='')
                    if playerPos != [-1,-1]:
                        if j == mapList[playerPos[1]][playerPos[0]]:
                            print(Back.RED, end='')
                    print(j.content, end='')
                else:
                    print(' ', end='')
                print(Style.RESET_ALL, end='')
            print()
    #def __init__(self):
    #    self.rooms = self.generate((int(input("Map width? ")),int(input("Map height? "))), int(input("Room Count? ")))
    #    self.rooms = self.createConnections(self.rooms)
    #    self.displayMap(self.rooms)
generator = Generator()