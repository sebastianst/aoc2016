#!/usr/bin/env python
# Read movements from file
mov=[x.strip() for x in open('input.txt', 'r').readline().split(',')]

# 1/-1 switch
def sign(x, val):
    return 1 if x == val else -1

# Initial state [0,0], heading north
P=[0, 0] # x, y
vP=[P.copy()] # vector of all visited locations
i=1 # index to move, 0(x) or 1(y)
s=1 # sign of direction
intersected = False
# Iterate over all movements
for m in mov:
    d=m[0] # R or L
    a=int(m[1:]) # number of steps
    s = s * sign(i, 1) * sign(d, 'R') # direction sign
    i = 0 if i else 1 # switch index
    for _ in range(a):
        P[i] += s
        if P in vP and not intersected:
            print('Second solution: %i' % sum(map(abs,P))) # L1 norm
            intersected = True
        else:
            vP.append(P.copy())

print('First solution: %i' % sum(map(abs,P))) # Taxi distance is L1 norm
