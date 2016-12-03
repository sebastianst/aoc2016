#!/usr/bin/env python
n,r,a = 0,0,[[0]*3]*3
valid = lambda t: all([(t[i%3] < t[(i+1)%3] + t[(i+2)%3]) for i in range(3)])

for line in open('input', 'r'):
    a[r] = [int(x) for x in line.split()]
    r = (r+1) % 3
    if not r: n += sum(map(valid,zip(*a)))

print(n)
