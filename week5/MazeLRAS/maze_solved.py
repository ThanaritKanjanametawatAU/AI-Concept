# The top part of this code is for reading input and illustration.
# Do not edit anything in this top part!
from vpython import *
scene.autoscale=False
i = 1
# Open the file for reading
with open(f"input/maze{i}.in", "r") as file:
    data = file.readlines()

# Strip unwanted spaces and newlines from the read data
data = [line.strip() for line in data]

M, N = map(int, data[0].split(' '))
sr, sc = map(int, data[1].split(' '))
dr, dc = map(int, data[2].split(' '))

scene.range = 6 * M

maze = [[0 for _ in range(N)] for _ in range(M)]
for i in range(M):
    x = data[i + 3].split(' ')
    for j in range(N):
        maze[i][j] = int(x[j])

# data = []
# M, N = map(int, input().split())
# sr, sc = map(int, input().split())
# dr, dc = map(int, input().split())
#
# scene.range = 6*M
#
# maze = []
# for _ in range(M):
#     row = list(map(int, input().split()))
#     maze.append(row)

# f = read_local_file(scene.title_anchor)
#
# data = []
# for line in f.text.split('\n'):
#     data.append(line[:-1])
#
# M,N = map(int, data[0].split(' '))
# sr,sc = map(int, data[1].split(' '))
# dr,dc = map(int, data[2].split(' '))

# scene.range = 6*M

# maze = [[0 for i in range(N)] for j in range(M)]
# for i in range(M):
#     x = data[i+3].split(' ')
#     for j in range(N):
#         maze[i][j] = int(x[j])  # set wall to -1 (so it won't mix with cost
        
mz = []
for i in range(M):
    a_row = []
    for j in range(N):
        if maze[i][j] == 0:
            cell = box(length=8, height=8, width=1, color=color.white)
        else:
            cell = box(length=8, height=8, width=1, color=color.blue)
        if i == dr and j == dc:
            cell.color = color.red
        cell.pos = vector((j-N//2)*10, -(i-M//2)*10, 0)
        a_row.append(cell)
    mz.append(a_row)

walker = cylinder(color=color.green, radius=3, pos=vector((sc-N//2)*10, -(sr-M//2)*10, 2), axis=vector(0,0,1)) 

# The solving code begins below this line

import random

adj = [(0,-1),(0,1),(-1,0),(1,0)]
H = [[None]*N for i in range(M)]

def manhatton(r, c):
    return abs(r-dr) + abs(c-dc)

def valid(r, c):
    if r < M and r >= 0 and c < N and c >= 0:
        if maze[r][c] == 0:
            return True
    return False

# ... [same top code to set up the visualization]

def move(cur, prev):
    best = None
    hBest = 100000000  # Just a large number to start with
    for d in adj:
        tr = cur[0] + d[0]
        tc = cur[1] + d[1]
        if valid(tr,tc):
            if H[tr][tc] is None:
                h = manhatton(tr, tc)
            else:
                h = H[tr][tc]

            # Update the heuristic for current position considering the neighboring costs
            current_h = H[cur[0]][cur[1]] if H[cur[0]][cur[1]] is not None else manhatton(cur[0], cur[1])
            if h < current_h - 1:
                h = current_h - 1

            if h < hBest:
                hBest = h
                best = (tr, tc)

    H[cur[0]][cur[1]] = hBest + 1
    return best, hBest

def lrtaStar():
    cur = (sr,sc)
    prev = (sr,sc)
    H[sr][sc] = manhatton(sr,sc)
    while cur != (dr,dc):
        prev = cur
        cur, h = move(cur, prev)
        walker.pos = vector((cur[1]-N//2)*10, -(cur[0]-M//2)*10, 2)
        rate(10)

lrtaStar()

