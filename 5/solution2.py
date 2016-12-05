#!/usr/bin/env python
from hashlib import md5

id, c, i = 'wtnhxymk', bytearray(8), 0

while not all(c):
    h = md5((id+str(i)).encode('ascii')).hexdigest()
    if h[:5] == 5*'0':
        pos = int(h[5], 16)
        if pos <= 8 and not c[pos]: c[pos] = ord(h[6])
    i += 1

print(c.decode('ascii'))
