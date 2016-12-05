#!/usr/bin/env python
import re
n,a = 0,ord('a')
room=re.compile(r'([a-z-]+)(\d+)\[([a-z]{5})\]')

for line in open('input', 'r'):
    r, k, c = room.match(line).groups()
    rs = r.replace('-','')
    cx = sorted([(-rs.count(x), x) for x in sorted(set(rs))])
    cm = ''.join(list(zip(*cx))[1][:5])
    if c == cm:
        k = int(k)
        n += k
        rd = [(ord(x)-a+k)%26 + a if x != '-' else ord(' ') for x in r[:-1]]
        rname = bytes(rd).decode('ascii')
        if rname.startswith('northpole'):
            print('northpole object storage:', k)

print('Valid room id sum:', n)
