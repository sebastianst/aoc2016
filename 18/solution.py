#!/usr/bin/env python
a, n = open('input', 'r').readline()[:-1], 0
W, a = len(a), [x=='^' for x in a]

def trap(a, i):
    c = a[i:i+3]
    return (sum(c)==2 and c[1]) or (sum(c)==1 and not c[1])

for _ in range(40):
    n += W - sum(a)
    a = [False] + a + [False]
    a = [trap(a,i) for i in range(W)]

print(n)
