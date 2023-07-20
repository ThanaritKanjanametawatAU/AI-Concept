
'''
Input format:
   line 1: number of time steps
   subsequent lines:
      the room that becomes dirty (0 for A, 1 for B, -1 for nothing happen)

'''

n = int(input())
room = 0   # in room A
dirty = [0,0]
count = 0
for t in range(n):
    r = int(input())
    if r != -1: # Something Happen
        dirty[r] = 1 #Room r becomes dirty
        if dirty[room] == 0: # If current room is not dirty
            room = (room+1)%2 # Move to another room
            count += 1 # Count actions (Move)
    if dirty[room] == 1: # If current room is dirty
        dirty[room] = 0   # sucked
        count += 1 # Count actions (Suck)
    print(dirty) # Check if room is cleaned
print(n, count) # Print Total Actions Performed ( Move and Suck)