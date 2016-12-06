#!/usr/bin/env python
code, code2 = '', ''

for col in zip(*open('input', 'r').readlines()):
    code += max(set(col), key=col.count)
    code2 += min(set(col), key=col.count)

print(code, code2, sep='')
