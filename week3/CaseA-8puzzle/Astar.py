
goal = [[0,1,2],[3,4,5],[6,7,8]]

p = []
for i in range(3):
    x = list(map(int, input().split()))
    p.append(x)

import copy
import sys
from simplePriorityQueue import Simple_Priority_Queue
sys.setrecursionlimit(10000)

adj = [(-1,0),(0,1),(1,0),(0,-1)]

def heuristic(p):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = p[i][j]
            if value != 0:
                goal_row, goal_col = divmod(value, 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance


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
        self.f = self.g + self.h  # Modified Here
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
            x.f = x.g + x.h  # Modified Here
            succ.append(x)
    return succ


def AstarSearch(s):  # Greedy Best-first Search
    global count

    # Complete the code below this line
    pq = Simple_Priority_Queue(lambda x,y: x.f<y.f)  # Modified Here
    pq.enqueue(s)
    Reached = set()
    Reached.add(s)

    count += 1
    while not pq.empty():
        node = pq.dequeue()
        if is_goal(node):
            return node

        for suc in successor(node):
            SInReached = False
            for d in Reached:
                if suc.p == d.p:
                    SInReached = True
                    break

            if not SInReached:
                suc.parant = node
                Reached.add(suc)
                pq.enqueue(suc)

                count += 1
    return None


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
v = AstarSearch(initial)
print(v.g, count)
print_path(initial, v)
