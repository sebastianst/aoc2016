#!/usr/bin/env python
import re
def decompress_len(inp):
    n = 0
    while len(inp):
        i = inp.find('(')
        if i == -1:
            n += len(inp)
            break
        n += i
        inp = inp[i:]
        a, b = re.match(r'\((\d+)x(\d+)\)', inp).groups()
        l = 3+len(a)+len(b)
        inp = inp[l:]
        n += int(b) * decompress_len(inp[:int(a)])
        inp = inp[int(a):]

    return n

print(decompress_len(open('input', 'r').readline()[:-1]))
