#!/usr/bin/env python
x,y,code = -2,0,''

pad = {(x,y): '{:X}'.format(x+o) for x in range(-2,3)
        for (y,o) in [(-2,1),(-1,3),(0,7),(1,11),(2,13)]}

for line in open('input', 'r'):
    for m in line:
        if   m == 'U': y -= (y-abs(x) > -2)
        elif m == 'D': y += (y+abs(x) < 2)
        elif m == 'L': x -= (x-abs(y) > -2)
        elif m == 'R': x += (x+abs(y) < 2)
    code += pad[(x,y)]

print(code)
