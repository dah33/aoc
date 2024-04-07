import re
from itertools import cycle
from math import lcm

f = open("./8.txt")
LR = f.readline().strip()
LR = [int(x) for x in LR.translate(str.maketrans("LR", "01"))]
next(f)
edges = [re.findall("[0-9A-Z]{3}", line) for line in f]
edges = {e[0]: (e[1], e[2]) for e in edges}


# Part 1
def path_length(node, end_suffix):
    global LR, edges
    for i, lr in enumerate(cycle(LR), 1):
        node = edges[node][lr]
        if node.endswith(end_suffix):
            break
    return i, node


print(path_length("AAA", "ZZZ")[0])

# Part 2
start_nodes = [n for n in edges.keys() if n.endswith("A")]

# Confirm cycles:
for start_node in start_nodes:
    length1, end_node1 = path_length(start_node, "Z")
    assert path_length(end_node1, "Z") == (length1, end_node1)

path_lengths = [path_length(n, "Z")[0] for n in start_nodes]
print(lcm(*path_lengths))
