#!/usr/bin/env python
from numpy import zeros, roll, count_nonzero
S = zeros((50,6), dtype=bool)

for line in open('input', 'r'):
    cmd, *args = line.split()
    if cmd == 'rect':
        x,y = map(int,args[0].split('x'))
        S[:x,:y] = True
    elif cmd == 'rotate':
        a, i, s = args[0], int(args[1][2:]), int(args[3])
        if a == 'row': S[:,i] = roll(S[:,i], s)
        else: S[i,:] = roll(S[i,:], s)

print(count_nonzero(S))
for row in S.transpose():
    print(*['*' if x else ' ' for x in row], sep='')
