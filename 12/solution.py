#!/usr/bin/env python
r,p,sw={'a':0,'b':0,'c':0,'d':0,},0,{'inc':1,'dec':-1}
I = [x[:-1].split() for x in open('input', 'r').readlines()]

while p < len(I):
    cmd = I[p]
    ins, x = cmd[0], cmd[1]
    if ins == 'cpy':
        x = r[x] if x in 'abcd' else int(x)
        r[cmd[2]] = x
    elif ins in sw:
        r[x] += sw[ins]
    elif ins == 'jnz':
        x = r[x] if x in 'abcd' else int(x)
        if x: p += int(cmd[2])-1
    p += 1

print(r['a'])
