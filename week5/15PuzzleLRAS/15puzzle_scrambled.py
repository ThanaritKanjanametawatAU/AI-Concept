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
d2idx = {'left':0, 'right':1, 'up':2, 'down':3}

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
        sleep(0.1)
    return hr,hc

hr,hc = scramble(0, 0, 40)
while True:
    ev = scene.waitfor('keydown')
    tr = hr + adj[d2idx[ev.key]][0]
    tc = hc + adj[d2idx[ev.key]][1]
    if valid(tr, tc):
        hr,hc = swap(hr, hc, tr, tc)

