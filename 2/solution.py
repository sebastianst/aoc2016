#!/usr/bin/env python
x,y,code = 2,1,''

for line in open('input', 'r'):
    for m in line:
        if   m == 'U': y -= (y>0)
        elif m == 'D': y += (y<2)
        elif m == 'L': x -= (x>1)
        elif m == 'R': x += (x<3)
    code += str(x+3*y)

print(code)
