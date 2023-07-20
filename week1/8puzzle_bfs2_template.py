goal = [[0,1,2],[3,4,5],[6,7,8]]

p = []   # the input pattern
for i in range(3):
    x = list(map(int, input().split()))
    p.append(x)

import copy
import sys

adj = [(-1,0),(0,1),(1,0),(0,-1)]   # relative positions around a position

def valid(r,c):
    return r >= 0 and r < 3 and c >= 0 and c < 3

class state:
    def __init__(self, p):
        self.p = copy.deepcopy(p)   # the board pattern
        self.g = 0                  # the number of moves so far
        self.parent = None          # the parent state

def is_goal(s):
    return s.p == goal

def hole_index(s):
    for i in range(3):
        for j in range(3):
            if s.p[i][j] == 0:
                return i,j


def successor(s):  # generates list of successor states of s
    succ = []
    hr, hc = hole_index(s)
    for d in adj:
        i = hr + d[0]
        j = hc + d[1]
        if valid(i,j):
            x = copy.deepcopy(s)
            x.p[hr][hc], x.p[i][j] = x.p[i][j], x.p[hr][hc]
            x.g += 1
            succ.append(x)
    return succ

def bfs(s):
    global count       # increments each time a state is enqueued

    # Complete the code below this line
    Q = [s]
    Reached = set()
    Reached.add(s)
    while Q:
        node = Q[0]
        del Q[0]

        for suc in successor(node):
            if is_goal(suc):
                return suc

            SInReached = False
            for d in Reached:
                if suc.p == d.p:
                    SInReached = True
                    break

            if not SInReached:
                suc.parent = node
                Reached.add(suc)
                Q.append(suc)
                count += 1

    return "Failure"

def print_path(s, v):  # s is the initial state, v is the current state
    if v.p==s.p:
        print(s.p)
    elif v.parent == None:
        print(f"No Path from {s.p} to {v.p} exists")
    else:
        print_path(s, v.parent)
        print(v.p)


count = 0
initial = state(p)
v = bfs(initial)
print(v.p)
print(v.g, count)      # prints the number of moves and total number of states generated
print_path(initial, v)
