#!/usr/bin/env python
code, code2 = '', ''

for col in zip(*open('input', 'r').readlines()):
    counts = sorted([ (col.count(x), x) for x in set(col) ])
    code += counts[-1][1]
    code2 += counts[0][1]

print(code[:-1])
print(code2[:-1])
