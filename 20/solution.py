#!/usr/bin/env python
rs = [ list(map(int,line.split('-'))) for line in open('input', 'r') ]
rs.sort()

u = -1
for r in rs:
    if r[0] > u+1:
        print(u+1)
        break
    u = max(u, r[1])
