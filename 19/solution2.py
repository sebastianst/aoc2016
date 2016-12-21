#!/usr/bin/env python
inp = 3004953
r = list(range(inp))
l = len(r)
while l > 1:
    i = 0
    while i < l:
        kick = (int(l/2)+i) % l
        r.pop(kick)
        l -= 1
        if kick > i: i += 1 # Don't increase index if we kicked smaller idx

print(r[0]+1)
