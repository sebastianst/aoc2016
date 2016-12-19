#!/usr/bin/env python
start, end, step = 1, 3004953, 1
while start < end:
    if ((start-end)/step % 2): #even
        end -= step
    else: # odd
        start += step*2
    step *= 2

print(start, end, step)
