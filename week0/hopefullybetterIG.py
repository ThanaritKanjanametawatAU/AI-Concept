class VacuumCleaner:
    def Left(self):
        V.actionCounter += 1


    def Right(self):
        V.actionCounter += 1


    def Suck(self):
        self.roomState[self.currentRoom] = 0
        V.actionCounter += 1

    def NoOP(self):
        print("No Operation Performed")

    def currentRoomIsDirty(self):
        return bool(self.roomState[self.currentRoom])

    def __init__(self):
        self.actionCounter = 0
        self.currentRoom = 0
        self.roomState = [0, 0]

n = int(input())
V = VacuumCleaner()
for _ in range(n):
    change = int(input())

    if change == -1:
        V.NoOP()
        continue

    V.roomState[change] = 1
    if V.currentRoomIsDirty(): # If current room is Dirty
        V.Suck()
    else:
        V.NoOP()

    if V.currentRoom:
        V.Left()
    else:
        V.Right()

    if V.currentRoomIsDirty():  # If current room is Dirty
        V.Suck()
    else:
        V.NoOP()

print(V.actionCounter)






