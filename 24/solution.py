#!/usr/bin/env python
M, poi = {}, {}
for y, line in enumerate(open('input', 'r')):
    for x, c in enumerate(line):
        if c in '01234567': poi[int(c)]=(x,y)
        M[(x,y)] = c!='#'
x_max, y_max = x, y

D = {}
def dist(a, b):
    """returns the shortest distance between POI a and POI b.
    Caches distances."""
    assert a in poi and b in poi
    a, b = min(a,b), max(a,b)
    if (a,b) not in D: D[(a,b)] = shortest(poi[a], poi[b])
    return D[(a,b)]

### from solution 13
# neighbours of node n
neigh = lambda n: {x for x in {(n[0]+1,n[1]),(n[0]-1,n[1]),(n[0],n[1]+1),(n[0],n[1]-1)}
            if x_max >= x[0] >= 0 and y_max >= x[1] >= 0 and M[n]}

def shortest(A, B):
    # Dijkstra, UCS (uniform-cost search) infinite graph optimization
    front, expl, steps = {A}, set(), 0 # Init
    while True:
        nfront = set()
        for node in front:
            if node == B:
                return steps
            expl.add(node)
            for n in neigh(node):
                if n not in expl and n not in front:
                    nfront.add(n)
        # Update
        front = nfront
        steps += 1
### end Dijkstra from solution 13

# Since there're only 6 points to visit, search all !6 possibilities...
def path_dist(path):
    d, a = 0, path[0]
    for b in path[1:]:
        d += dist(a, b)
        a = b
    return d

def shortest_dist(path, rt=False):
    if len(path) == 8:
        if rt: path.append(path[0])
        return path_dist(path)
    else:
        remaining = list(range(8))
        for p in path: remaining.remove(p)
        return min([shortest_dist(path + [x], rt) for x in remaining])

print(shortest_dist([0]))
print(shortest_dist([0], True))
