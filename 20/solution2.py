#!/usr/bin/env python
rs = [ list(map(int,line.split('-'))) for line in open('input', 'r') ]
rs.sort()

u, n = -1, 0
for r in rs:
    if r[0] > u+1:
        n += r[0] - u -1
    u = max(u, r[1])

print(n)
