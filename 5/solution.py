#!/usr/bin/env python
from hashlib import md5

id, c, i = 'wtnhxymk', '', 0

while len(c) < 8:
    h = md5((id+str(i)).encode('ascii')).hexdigest()
    if h[:5] == 5*'0': c += h[5]
    i += 1

print(c)
