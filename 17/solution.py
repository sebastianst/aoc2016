#!/usr/bin/env python
from hashlib import md5
from copy import copy
inp = b'njfxhljp'
DIR = {'U':1j, 'D':-1j, 'L':-1, 'R':1}

class Loc():
    path = ''
    pos = 0j
    def go(self, d):
        L = copy(self)
        L.path += d
        L.pos += DIR[d]
        return L
    def open_neigh(self):
        h = md5(inp + self.path.encode()).digest()[:2]
        h = h[0]*256 + h[1]
        neigh = [ self.go('RLDU'[i]) for i in range(4) if h//(16**i) %16 > 10 ]
        return [n for n in neigh if (0<=n.pos.real<4 and 0>=n.pos.imag>-4)]
    def cost(self):
        """Let the cost be the length of the path plus the 1-l distance to the
        vault (negative and shifted)"""
        return (self.pos.real - self.pos.imag) - len(self.path)

front = [Loc()]
while True:
    if not front:
        print("There's no path to the vault :(")
        break
    front = sorted(front, key=Loc.cost)
    l = front.pop()
    if l.pos == 3-3j:
        print(l.path)
        break
    for f in l.open_neigh():
        front.append(f)
