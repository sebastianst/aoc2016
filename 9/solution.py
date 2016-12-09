#!/usr/bin/env python
import re
output = ''
inp = open('input', 'r').readline()[:-1] # omit \n
while len(inp):
    c=inp[0]
    if c != '(':
        output += c
        inp = inp[1:]
    else:
        a, b = re.match(r'\((\d+)x(\d+)\)', inp).groups()
        l = 3+len(a)+len(b)
        inp = inp[l:]
        output += int(b) * inp[:int(a)]
        inp = inp[int(a):]

print(len(output))
