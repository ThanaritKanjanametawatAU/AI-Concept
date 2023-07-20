
goal = [[0,1,2],[3,4,5],[6,7,8]]

p = []
for i in range(3):
    x = list(map(int, input().split()))
    p.append(x)

import copy
import sys

adj = [(-1,0),(0,1),(1,0),(0,-1)]

def heuristic(p):
    mht = 0
    for i in range(3):
        for j in range(3):
            if p[i][j] != 0:
                r = p[i][j]//3
                c = p[i][j]%3
                mht += abs(i-r) + abs(j-c)
    return mht

def valid(r,c):
    if r >= 0 and r < 3 and c >= 0 and c < 3:
        return True
    else:
        return False

class state:
    def __init__(self, p):
        self.p = copy.deepcopy(p)
        self.g = 0
        self.h = heuristic(p)
        self.f = self.g + self.h
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
            x.h = heuristic(x.p)
            x.f = x.g + x.h
            succ.append(x)
    return succ

def DFS(s, atMost):
    global count, found
    
    if s.f > atMost:
        return s
    elif is_goal(s):
        found = True
        return s
    else:
        count += 1
        atLeast = sys.maxsize
        for n in successor(s):
            v = DFS(n, atMost)
            if v.f < atLeast:
                atLeast = v.f
                u = v
            if found:
                break
        return u



def IDastar(s):
    global found
    bound = s.f
    result = DFS(s, 0)
    while not is_goal(result):
        bound = result.f
        result = DFS(s, bound)

    return result

def print_path(s, v):  # s is the initial state, v is the current state
    if v.p==s.p:
        print(s.p)
    elif v.parent == None:
        print(f"No Path from {s.p} to {v.p} exists")
    else:
        print_path(s, v.parent)
        print(v.p)

found = False
count = 0
initial = state(p)
v = IDastar(initial)
print(v.g, count)
print_path(initial, v)
