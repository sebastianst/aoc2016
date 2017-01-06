#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser(description='Solution to puzzle 21 of the Advent of Code 2016')
parser.add_argument('-u', '--unscramble', action='store_true')
parser.add_argument('-i', '--input')
args = parser.parse_args()
unscr = args.unscramble
s = args.input
if not s: s = 'fbgdceah' if unscr else 'abcdefgh'
l = len(s)

def swap_pos(x, y):
    global s, unscr
    v = list(s)
    v[x] = s[y]
    v[y] = s[x]
    s = ''.join(v)

def swap_let(a, b):
    global s, unscr
    swap_pos(*map(s.find, [a, b]))

def rotate(k):
    global s, unscr
    if unscr: k = -k
    k = k%l
    if k > 0: s = s[-k:] + s[:-k]

def rotate_let(a):
    global s, unscr
    i = s.find(a)
    k = {0:1,1:1,2:6,3:2,4:7,5:3,6:0,7:4}[i] if unscr else i + 1 + k>4
    rotate(k)

def reverse(x, y):
    global s, unscr
    rev = s[y:x-1:-1] if x else s[y::-1]
    s = s[:x] + rev + s[y+1:]

def move(x, y, rev=False):
    global s, unscr
    if not rev and unscr:
        move(y, x, rev=True)
    else:
        if x < y: s = s[:x] + s[x+1:y+1] + s[x] + s[y+1:]
        if y < x: s = s[:y] + s[x] + s[y:x] + s[x+1:]

inp = open('input', 'r').readlines()
if unscr: inp = inp[::-1]
for line in inp: # TODO check rotate based on letter
    print(s)
    print(line)
    cmd, sub, *args = line.split()
    if cmd == 'swap':
        x, y = args[0], args[3]
        if sub == 'position': swap_pos(int(x), int(y))
        else: swap_let(x, y)
    elif cmd == 'rotate':
        if sub == 'based':
            rotate_let(args[4])
        else:
            k = int(args[0])
            if sub == 'left': k *= -1
            rotate(k)
    elif cmd == 'reverse':
        reverse(int(args[0]), int(args[2]))
    elif cmd == 'move':
        move(int(args[0]), int(args[3]))

print(s)
