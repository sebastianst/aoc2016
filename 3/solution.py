#!/usr/bin/env python
n = 0
for line in open('input', 'r'):
    t = [int(x) for x in line.split()]
    n += all([(t[i%3] < t[(i+1)%3] + t[(i+2)%3]) for i in range(3)])

print(n)
