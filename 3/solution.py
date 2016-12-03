#!/usr/bin/env python
n = 0
for line in open('input', 'r'):
    a = [int(x) for x in line.split()]
    p = True
    for i in range(3):
        p &= (a[i%3] < a[(i+1)%3] + a[(i+2)%3])
    n += p

print(n)
