import copy
import re

parse_row = lambda s: s[1 : len(s) : 4]
stacks = None
f = open("./5.txt")
for line in f:
    row = parse_row(line)
    if row[0].isdigit():
        break
    if not stacks:
        stacks = [[]] * len(row)
    for i, c in enumerate(row):
        if c != " ":
            stacks[i] = [c] + stacks[i]

next(f)
moves = [tuple(map(int, re.findall("(\d+)", line))) for line in f]
f.close()

stacks_backup = copy.deepcopy(stacks)

for c, f, t in moves:
    for _ in range(c):
        stacks[t - 1].append(stacks[f - 1].pop())
print("".join([s.pop() for s in stacks]))

stacks = ["".join(s) for s in stacks_backup]
for c, f, t in moves:
    pop, stacks[f - 1] = stacks[f - 1][-c:], stacks[f - 1][:-c]
    stacks[t - 1] += pop
print("".join([s[-1] for s in stacks]))
