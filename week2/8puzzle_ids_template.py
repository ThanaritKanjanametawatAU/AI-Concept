import sys
sys.setrecursionlimit(10000)
goal = [[0,1,2],[3,4,5],[6,7,8]]

p = []
for i in range(3):
    x = list(map(int, input().split()))
    p.append(x)

import copy
import sys

adj = [(-1,0),(0,1),(1,0),(0,-1)]

def valid(r,c):
    if r >= 0 and r < 3 and c >= 0 and c < 3:
        return True
    else:
        return False

class state:
    def __init__(self, p):
        self.p = copy.deepcopy(p)
        self.g = 0
        self.parent = None

def is_goal(s):
    if s.p == goal:
        return True
    else:
        return False

def hole_index(s):
    for i in range(3):
        for j in range(3):
            if s.p[i][j] == 0:
                return i,j

def successor(s):
    succ = []
    hr, hc = hole_index(s)
    for d in adj:
        i = hr + d[0]
        j = hc + d[1]
        if valid(i,j):
            x = copy.deepcopy(s)
            x.p[hr][hc], x.p[i][j] = x.p[i][j], x.p[hr][hc]
            x.parent = s
            x.g += 1
            succ.append(x)
    return succ


def DFS(s, maxDepth):  # depth is limited to be <= maxDepth
    global count  # increments when state s is depth-first searched

    if s.g > maxDepth:
        return None
    elif is_goal(s):
        return s
    else:
        count += 1
        for n in successor(s):
            v = DFS(n ,maxDepth)
            if v != None:
                return v
        return None

def IDS(s):
    depth = 0
    result = DFS(s, 0)
    while result == None:
        depth += 1
        result = DFS(s, depth)
    return result

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
v = IDS(initial)
print(v.g, count)
print_path(initial, v)
