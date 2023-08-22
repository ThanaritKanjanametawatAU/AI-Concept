# The top part is for illustration and scrambling puzzle
# Do not edit this top part!

from vpython import *

scene.height = scene.width = 600
scene.range = 160
scene.autoscale = False

board = box(pos=vector(0,0,0), color=vector(0.9,0.75,0.75), height=180, length=180, width=1)

class a_tile:
    def move_to(self, r, c):
        self.base.pos = vector(c*40+20-80, 40-r*40+20, 2)
        self.label.pos = self.base.pos + vector(-1,-10,2)
        
    def move_to_pos(self, x, y):
        self.base.pos = vector(x, y, 2)
        self.label.pos = self.base.pos + vector(-1,-10,2)
        
    def __init__(self, number):
        self.base = box(height=38, length=38, width=5, color=color.blue)
        self.number = number
        self.r = number//4
        self.c = number%4
        self.label = text(text=str(self.number), align='center', color=color.white, height=20, depth=1) 
        self.move_to(self.r, self.c)
        if self.number == 0:
            self.base.visible = self.label.visible = False


tile = []
for i in range(16):
    tile.append(a_tile(i))

def swap_tile(a,b):
    xa, ya = tile[a].base.pos.x, tile[a].base.pos.y
    xb, yb = tile[b].base.pos.x, tile[b].base.pos.y
    tile[a].move_to_pos(xb, yb)
    tile[b].move_to_pos(xa, ya)

p = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]

adj = [(0,-1),(0,1),(-1,0),(1,0)]

def valid(r, c):
    if r < 4 and r >= 0 and c < 4 and c >= 0:
        return True
    else:
        return False

def swap(hr, hc, tr, tc):
    swap_tile(p[hr][hc], p[tr][tc])
    p[hr][hc] = p[tr][tc]
    p[tr][tc] = 0
    hr, hc = tr, tc
    return hr, hc

import random

def scramble(hr, hc, n):
    for i in range(n):
        t = random.randint(0,10000)%4
        tr = hr + adj[t][0]
        tc = hc + adj[t][1]
        if valid(tr,tc):
            hr, hc = swap(hr, hc, tr, tc)
        rate(10)
    return hr,hc

adj = [(0,-1),(0,1),(-1,0),(1,0)]

# Solving code begins below this line.

H = {}  # The dictionary to record the visited state

def heuristic(p):
    # Sum of manhatton distances between each tile and its target position
    mht = 0
    for i in range(4):
        for j in range(4):
            if p[i][j] != 0:
                r = p[i][j]//4
                c = p[i][j]%4
                mht += abs(i-r) + abs(j-c)
    return mht

class state:
    def __init__(self, p):
        self.p = []
        for row in p:
            self.p.append(row[:])
        self.h = heuristic(p)

def hole_index(s):
    for i in range(4):
        for j in range(4):
            if s.p[i][j] == 0:
                return i,j

def successor(s):
    succ = []
    hr, hc = hole_index(s)
    for d in adj:
        i = hr + d[0]
        j = hc + d[1]
        if valid(i,j):
            x = state(s.p)
            x.p[hr][hc], x.p[i][j] = x.p[i][j], x.p[hr][hc]
            x.h = heuristic(x.p)
            succ.append(x)
    return succ

def p2tuple(p):  # Return an equivalent tuple for a 2D list
    t = []
    for row in p:
        t.append(tuple(row))
    return tuple(t)


def move(s, h0):
    best = None
    hBest = float("inf")  # Initialize to infinity
    succ = successor(s)
    for u in succ:
        t = p2tuple(u.p)
        th = H.get(t, u.h)  # If not found in H, use heuristic value of u

        if th < hBest:
            hBest = th
            best = u

    # Update heuristic for the current state
    current_state_tuple = p2tuple(s.p)
    if hBest < float("inf"):
        H[current_state_tuple] = hBest + 1  # Assuming each move has a cost of 1

    succ.clear()
    return best, hBest


def lrtaStar():
    global hr, hc  # Make sure to use the global hr and hc variables
    s = state(p)
    h = s.h
    H[p2tuple(s.p)] = h
    prev_r = hr
    prev_c = hc

    # Loop-limiting counter to break out of infinite loops (for debugging)
    counter = 0

    while s.h != 0:
        if counter > 500:  # Adjust this value as necessary
            print("Exiting due to loop. Needs debugging.")
            break

        s, h = move(s, h)  # Make one move (update s and h)
        tr, tc = hole_index(s)
        prev_r, prev_c = swap(prev_r, prev_c, tr, tc)

        rate(10) # Sleep for 10ms

        counter += 1  # Increment loop counter



hr,hc = scramble(0, 0, 50)   # Scramble with 40 random moves
print("SOLVING!")
sleep(2)
lrtaStar()
