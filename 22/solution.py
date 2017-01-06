#!/usr/bin/env python
import re
inp, n, node = open('input', 'r'), 0, {}
inp.readline()
inp.readline()

for line in inp:
    x, y, size, used = [int(x) for x in
            re.match(r'\/dev\/grid\/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T.*',
                line).groups()]
    node[(x,y)] = {'size': size, 'used': used}

node1 = node.copy()
n_fat, wx = [], None
for (Ak, Av) in node.items():
    # Part I
    if Av['used'] > 0:
        del node1[Ak]
        for (Bk, Bv) in node1.items():
            n += Av['used'] <= (Bv['size'] - Bv['used'])
    # Part II - collect special nodes
    if Av['used'] == 0: n_empty = Ak
    if Av['size'] > 100: wx = min(wx, Ak[0]) if wx else Ak[0]

print('Solution 1: %i' % n)

### Part II
dx = max([x[0] for x in node.keys()]) # No hardcoded max x
# Shortest solution: Move
#  1. gap to the left of fat node wall,
#  2. gap to the right, 1 left of target x coord,
#  3. gap to the top row.
#  3. Use 5-circle-movements to move target data one step at a time to the left.
#  4. Finally one move of the data to (0,0).
# Assertions: * One gap only (with x coord = max(x)-1)
#   * fat nodes form a wall from the left border
assert dx-1 == n_empty[0] # to remove abs(dx - n_empty[0])
m = 2*(dx-wx) + n_empty[1] + 5*(dx-1) + 1
print('Solution 2: %i' % m)
