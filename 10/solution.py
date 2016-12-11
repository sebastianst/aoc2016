#!/usr/bin/env python
low, high, chip = {}, {}, {} # low and high mappings, chip location state

def give_chip(target, value, source=None):
    global chip
    if target in chip: chip[target].add(value)
    else: chip[target] = {value}
    if source: chip[source].remove(value)

for line in open('input', 'r'):
    l = line.split()
    if l[0] == 'value':
        t, v = [int(l[i]) for i in [5,1]]
        give_chip((t, 'bot'), v)
    if l[0] == 'bot':
        bot, lo, hi = [(int(l[i]), l[i-1]) for i in [1,6,11]]
        low[bot], high[bot] = lo, hi

while True:
    c = [b for b, v in chip.items() if len(v)==2 and b[1]=='bot']
    if len(c) > 0: c = c[0]
    else: break

    if chip[c] == {61, 17}:
        print('Bot %i is the winner!' % c[0])
    give_chip(low[c], min(chip[c]), c)
    give_chip(high[c], max(chip[c]), c)

o = [chip[(i, 'output')].pop() for i in [0,1,2]]
print('Product of Outputs 0, 1, 2: %i' % (o[0]*o[1]*o[2]))
