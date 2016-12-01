#!/usr/bin/env python
import curses
from curses import *
from time import sleep

# 1/-1 switch
def sign(x, val):
    return 1 if x == val else -1

def padsize(vP):
    y = max([p[1] for p in vP]) - min([p[1] for p in vP]) + 2
    x = max([p[0] for p in vP]) - min([p[0] for p in vP]) + 2
    return (y, x)

def align_pad(pad, visible_y, visible_x):
    pad_lines, pad_cols = pad.getmaxyx()
    border_width = max(curses.COLS - pad_cols, 0)
    border_heigth = max(curses.LINES - pad_lines, 0)
    hidden_width = max(pad_cols - curses.COLS , 0)
    hidden_heigth = max(pad_lines - curses.LINES, 0)

    x = hidden_width // 2
    if visible_x > curses.COLS + x:
        x = visible_x - curses.COLS
    elif visible_x < x:
        x = visible_x

    y = hidden_heigth // 2
    if visible_y > curses.LINES + y:
        y = visible_y - curses.LINES
    elif visible_y < y:
        y = visible_y

    pad.refresh(y, x,
            border_heigth // 2, border_width // 2,
            curses.LINES - border_heigth // 2 - 1, curses.COLS - border_width // 2 - 1)

def main(scr):
    # Read movements from file
    mov=[x.strip() for x in open('input.txt', 'r').readline().split(',')]
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

    # ncurses init
    scr.clear()
    pad = newpad(*padsize(vP))
    # rescale all points to fit into the pad coord system, switch x,y
    min_x = min([p[0] for p in vP])
    min_y = min([p[1] for p in vP])
    vQ = [[p[1]-min_y, p[0]-min_x] for p in vP]
    for q in vQ:
        pad.addstr(*q, '*')
        align_pad(pad, *q)
        sleep(.1)

wrapper(main)
