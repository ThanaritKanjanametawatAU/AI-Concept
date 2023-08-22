import copy
import sys
from simplePriorityQueue import Simple_Priority_Queue
sys.setrecursionlimit(10000)

h = int(input())
heuristicsVal = {}
for _ in range(h):
    a, b = input().split()
    heuristicsVal[a] = int(b)

e = int(input())
adj_list = {}
for _ in range(e):
    a, b, c = input().split()
    if a in adj_list.keys():
        adj_list[a].append((b, int(c)))
    else:
        adj_list[a] = [(b, int(c))]

    if b in adj_list.keys():
        adj_list[b].append((a, int(c)))
    else:
        adj_list[b] = [(a, int(c))]

print(heuristicsVal)
print(adj_list)

def heuristic(p):
    return heuristicsVal[p]

class state:
    def __init__(self, p):
        self.p = copy.deepcopy(p)
        self.g = 0
        self.h = heuristic(p)
        self.parent = None

def is_goal(s):
    return heuristicsVal[s] == 0


def UCS(s):
    global count
    # Complete the code below this line
    pq = Simple_Priority_Queue(lambda x,y: x.g<y.g)
    pq.enqueue(s)
    Reached = set()
    Reached.add(s)

    count += 1
    while not pq.empty():
        node = pq.dequeue()
        if is_goal(node):
            return node
        Reached.add(node)
        for suc, cost in adj_list[node]:
            if suc not in Reached:
                suc.parant = node
                suc.g += cost
                suc.h = heuristic(suc)
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
v =UCS(initial)
print(v.g, count)
print_path(initial, v)



