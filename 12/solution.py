#!/usr/bin/env python
r,p,sw={'a':0,'b':0,'c':0,'d':0,},0,{'inc':1,'dec':-1}
I = [x[:-1].split() for x in open('input', 'r').readlines()]

while p < len(I):
    cmd = I[p]
    ins, x = cmd[0], cmd[1]
    if ins in sw:
        r[x] += sw[ins]
    else:
        x = r[x] if x in 'abcd' else int(x)
        if ins == 'cpy':
            r[cmd[2]] = x
        elif ins == 'jnz':
            if x: p += int(cmd[2])-1
    p += 1

print(r['a'])
