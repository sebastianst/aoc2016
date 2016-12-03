#!/usr/bin/env python
n,r = 0,0
a,b,c = [0,0,0],[0,0,0],[0,0,0]
def valid(a):
    p = True
    for i in range(3):
        p &= (a[i%3] < a[(i+1)%3] + a[(i+2)%3])
    return p

for line in open('input', 'r'):
    a[r], b[r], c[r] = [int(x) for x in line.split()]
    r = (r+1) % 3
    if not r: n += sum(map(valid,[a,b,c]))

print(n)
