#!/usr/bin/env python
inp, length = '11011110011011101', 35651584 # length = 272 for part 1

inv = lambda s: s.replace('0','x').replace('1','0').replace('x','1')[::-1]
while len(inp) < length:
    inp = inp + '0' + inv(inp)

inp = inp[:length]

while len(inp) % 2 == 0:
    c = ''
    for i in range(0, len(inp), 2):
        c += str(int(inp[i] == inp[i+1]))
    inp = c

print(inp)
