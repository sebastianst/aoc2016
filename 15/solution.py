#!/usr/bin/env python
from sympy.ntheory.modular import crt

z=list(zip(*[ x[:-2].split() for x in open('input','r').readlines() ]))
m, N=list(map(int,z[3])), len(z[0])
v=[-(int(z[11][i])+1+i) for i in range(N)]

print(crt(m, v))
# Part 2
print(crt(m+[11],v+[-N-1]))
