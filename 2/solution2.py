#!/usr/bin/env python
input = open('input', 'r')

x,y,code = -2,0,''

pad = {(0,-2): 1,
        (-1,-1): 2, (0,-1): 3, (1,-1): 4,
        (-1,1): 'A', (0,1): 'B', (1,1): 'C',
        (0,2): 'D'}

for i in range(-2,3):
    pad[(i,0)] = i+7

for line in input:
    for m in line:
        if m == 'U':
            y -= (y-abs(x) > -2)
        elif m == 'D':
            y += (y+abs(x) < 2)
        elif m == 'L':
            x -= (x-abs(y) > -2)
        elif m == 'R':
            x += (x+abs(y) < 2)
    code += str(pad[(x,y)])

print(code)
