#!/usr/bin/env python
import re
n, m = 0, 0
abba = lambda s: any([s[i]==s[i+3] and s[i+1]==s[i+2] and s[i]!=s[i+1] for i in range(len(s)-3)])
def ssl(s, h):
    aba = [x[i+1:i+3]+x[i+1] for x in s for i in range(len(x)-2) if x[i]==x[i+2]]
    return any([x in y for x in aba for y in h])
for line in open('input', 'r'):
    a = re.match('([a-z]+)' + '\[([a-z]+)\]([a-z]+)'*line.count('['), line).groups()
    s, h = a[0::2], a[1::2]
    n += (any(map(abba,s)) and not any(map(abba,h)))
    m += ssl(s, h)

print(n)
print(m)
