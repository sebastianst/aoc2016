#!/usr/bin/env python
inp = 1350
def is_wall(p):
    x,y=p[0],p[1]
    z = x*x + 3*x + 2*x*y + y + y*y + inp
    return bool('{:b}'.format(z).count('1') % 2)

# neighbours of node n
neigh = lambda n: {x for x in {(n[0]+1,n[1]),(n[0]-1,n[1]),(n[0],n[1]+1),(n[0],n[1]-1)}
            if x[0] >= 0 and x[1] >= 0 and not is_wall(x)}

# Dijkstra, UCS (uniform-cost search) infinite graph optimization
front, expl, steps, found = {(1,1)}, set(), 0, False # Init
while not found:
    nfront = set()
    for node in front:
        # Part 1
        if node == (31,39):
            print(steps)
            found = True # assume steps >= 50
            break
        expl.add(node)
        for n in neigh(node):
            if n not in expl and n not in front:
                nfront.add(n)
    # Part 2
    if steps == 50:
        print('In <= 50 steps we can reach %i locs' % (len(expl)))
    # Update
    front = nfront
    steps += 1
