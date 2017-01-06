#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser(description='Solution to puzzle 23 of the Advent of Code 2016')
parser.add_argument('-a', type=int, default=7)
parser.add_argument('-i', '--input', default='input')
args = parser.parse_args()

r,p,sw={'a':args.a,'b':0,'c':0,'d':0,},0,{'inc':1,'dec':-1}
I = [x.split() for x in open(args.input, 'r').readlines()]

while p < len(I):
    cmd = I[p]
    ins, x = cmd[0], cmd[1]
    if len(cmd) == 3: y = cmd[2]
    if ins in sw:
        r[x] += sw[ins]
    else:
        x = r[x] if x in 'abcd' else int(x)
        if ins == 'cpy':
            if y in r: r[y] = x # tgl may invalidate instruction
        elif ins == 'jnz':
            y = r[y] if y in 'abcd' else int(y)
            if x: p += y-1
        elif ins == 'tgl' and 0 <= p+x < len(I):
            tI = I[p+x]
            # one argument instructions
            if len(tI) == 2:
                tI[0] = 'dec' if tI[0] == 'inc' else 'inc'
            # two-argument instructions
            else:
                tI[0] = 'cpy' if tI[0] == 'jnz' else 'jnz'
    p += 1

print(r['a'])
