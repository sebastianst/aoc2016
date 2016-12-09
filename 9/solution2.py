#!/usr/bin/env python
import re
def decompress_len(inp):
    n = 0
    while len(inp):
        c=inp[0]
        if c != '(':
            n += 1
            inp = inp[1:]
        else:
            a, b = re.match(r'\((\d+)x(\d+)\)', inp).groups()
            l = 3+len(a)+len(b)
            inp = inp[l:]
            n += int(b) * decompress_len(inp[:int(a)])
            inp = inp[int(a):]

    return n

print(decompress_len(open('input', 'r').readline()[:-1]))
