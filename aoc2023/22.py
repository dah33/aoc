import re
from collections import defaultdict

blocks = [tuple(map(int, re.findall("(\d+)", l))) for l in open("./22.txt")]
N = len(blocks)

# order blocks by z_order so we land lower blocks first
z_order = lambda b: b[2]
blocks = sorted(blocks, key=z_order)

under = defaultdict(set)
over = defaultdict(set)
heights = defaultdict(int)
occupier = {}
for i, coords in enumerate(blocks):
    x1, y1, z1, x2, y2, z2 = coords
    floor = max(heights[(x, y)] for x in range(x1, x2 + 1) for y in range(y1, y2 + 1))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            heights[(x, y)] = floor + (z2 - z1 + 1)
            foot = (x, y, floor)
            if foot in occupier:
                below = occupier[foot]
                under[i].add(below)
                over[below].add(i)
            for z in range(floor + 1, floor + (z2 - z1 + 1) + 1):
                occupier[(x, y, z)] = i


def n_disintegrated(start):
    todo = {start}
    done = set()
    while todo:
        leg = todo.pop()
        done.add(leg)
        unsupported = set(above for above in over[leg] if under[above].issubset(done))
        todo |= unsupported
    return len(done)


# Part 1 variant
print(sum(n_disintegrated(i) == 1 for i in range(N)))

# Part 2
print(sum(n_disintegrated(i) - 1 for i in range(N)))

# Lessons
# - Should draw by hand simple example to work through
# - Writing in English is a great first help
# - Since blocks are unlabelled, enumerating is best, so use lists
# - part 2 answer made part 1 easier to conceptualise!
# - rewrote to use defaultdict to simplify
# - was worried about computational complexity, but it's tiny!
