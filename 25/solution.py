#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser(description='Solution to puzzle 25 of the Advent of Code 2016')
parser.add_argument('-a', type=int, default=None)
parser.add_argument('-i', '--input', default='input')
args = parser.parse_args()

sw={'inc':1,'dec':-1}
I = [x.split() for x in open(args.input, 'r').readlines()]

def check_a(a):
    print('Trying a=%i' % a)
    r, p = {'a':a,'b':0,'c':0,'d':0,}, 0
    clock, count = 1, 0
    while p < len(I):
        cmd = I[p]
        ins, x = cmd[0], cmd[1]
        if len(cmd) == 3: y = cmd[2]
        if ins in sw:
            r[x] += sw[ins]
        else:
            x = r[x] if x in 'abcd' else int(x)
            if ins == 'cpy':
                if y in r: r[y] = x
            # 'add x y' adds x/r[x] to register y (new instruction)
            elif ins == 'add':
                r[y] += x
            elif ins == 'jnz':
                y = r[y] if y in 'abcd' else int(y)
                if x: p += y-1
            elif ins == 'out':
                count += 1
                print('[%i] a = %i, b = %i' % (count, r['a'], r['b']))
                if not x ^ clock:
                    print('[a=%i] Wrong clock signal after iteration %i' % \
                            (r['a'], count))
                    return False
                clock = x
                if r['a'] == 0: return True
        p += 1

if args.a != None:
    check_a(args.a)
else:
    a = 0
    while not check_a(a): a += 1
    print('Minimum a = %i' % a)
