import random
import re
from math import ceil, sqrt


def copy_dict(E):
    return {k: v.copy() for k, v in E.items()}


def contract(V, E, t):
    """Removes edges at random until size <= t; modifies V and E"""
    while len(V) > t:
        # Select edge at random, but note not uniformly random
        u = random.choice(tuple(E.keys()))
        v = random.choice(E[u])

        # Merge vertices u and v
        E[u].extend(E[v])
        del E[v]

        # Update partitions
        V[u] = V[u].union(V[v])
        del V[v]

        # Replace all occurrences of v with u in the graph
        for vertex in E:
            E[vertex] = [u if x == v else x for x in E[vertex]]

        # Remove self loops
        E[u] = [x for x in E[u] if x != u]

    return


def _karger_min_cut(V, E):
    """Returns the cut size, modifies V and E"""
    contract(V, E, 2)
    cut = len(E[list(E.keys())[0]])
    return cut, V, E


def _karger_stein_min_cut(V, E):
    """Returns the cut size, modifies V and E"""
    # TODO: is about 3x slower than the karger min cut, likely due to
    # inefficiencies in Python!
    assert len(E) == len(V)
    if len(E) <= 6:
        return _karger_min_cut(V, E)
    else:
        t = ceil(1 + len(E) / sqrt(2))
        E2, V2 = copy_dict(E), copy_dict(V)
        contract(V, E, t)
        contract(V2, E2, t)
        cut1, V, E = _karger_stein_min_cut(V, E)
        cut2, V2, E2 = _karger_stein_min_cut(V2, E2)
        if cut1 < cut2:
            return cut1, V, E
        else:
            return cut2, V2, E2


def min_cut(E, strategy=_karger_min_cut):
    """Returns the cut size and 2 partitions; doesn't modify E"""
    E = copy_dict(E)
    V = {u: {u} for u in E}  # map of current vertices to originals
    cut, V, E = strategy(V, E)
    return cut, tuple(V.values())  # V is now two nodes, each a partition


# Load graph from file
cn = [re.findall("\w+", l) for l in open("./25.txt")]
E = {a: B for a, *B in cn}
for b, *A in cn:
    for a in A:
        E.setdefault(a, []).append(b)

# Simple example graph, abc in triangle with a->d
# a, b, c, d = tuple("abcd")
# E = {}
# E[a] = [b, c, d]
# E[b] = [a, c]
# E[c] = [a, b]
# E[d] = [a]


# Run the Karger's algorithm many times to find the min. cut
best_cut = float("inf")
best_partition = None
while best_cut > 3:
    cut, partition = min_cut(E)
    if cut < best_cut:
        best_cut = cut
        best_partition = partition

best_score = len(best_partition[0]) * len(best_partition[1])
print(best_score)

# Lessons
# - First time I've looked at graph algorithms, so I decided to implement
#   Karger's algorithm to maximise my learning.
# - My original implementation using a set of vertices (u,v) was very slow for
#   the real puzzle input, but the vertex->edge-list version was easily fast
#   enough.
# - It was also possible to visualise the graph, and easily see the three edges
#   to cut. You'd then need an algorthm to determine the nodes in each
#   partition, or possibly networkx has something appropriate. See
#   './25-how-to.md'
# - 4HbQ's ad hoc solution is genius, kinda like flood-fill, always taking next
#   highest connected.
# - Another ad hoc solution was to pick random pairs of nodes, find paths
#   between them, then look at which nodes are most common on paths. You'd
#   expect one edge from 3-edge-bridge to appear in about half the paths (as
#   you've randomly picked nodes on either side of the bridge).

# xelf's networkx solution:
from math import prod

import networkx as nx

G = nx.Graph()
G.add_edges_from(
    (k, i) for r in open("./25.txt") for k, v in [r.split(":")] for i in v.split()
)
G.remove_edges_from(nx.minimum_edge_cut(G))
print(prod(map(len, nx.connected_components(G))))

# 4HbQ's igraph solution, ungolfed:
from math import prod

import igraph as ig

G = ig.Graph.ListDict(
    {v: e.split() for v, e in [l.split(":") for l in open("./25.txt")]}
)
print(prod(G.mincut().sizes()))

# Plotting code:
layout = G.layout("kk")  # Kamada-Kawai layout for nice graph aesthetics
plot = ig.plot(G, layout=layout, vertex_label=G.vs["name"], bbox=(3000, 3000))
plot.save("25.png")

import os

# Display with Linux:
os.system("feh 25.png")
# Display with Windows:
os.system("explorer.exe 25.png")

# 4HbQ's ad hoc solution:

import collections as C

G = C.defaultdict(set)

for line in open("./25.txt"):
    u, *vs = line.replace(":", "").split()
    for v in vs:
        G[u].add(v)
        G[v].add(u)


S = set(G)

count = lambda v: len(G[v] - S)

while sum(map(count, S)) != 3:
    S.remove(max(S, key=count))

print(len(S) * len(set(G) - S))

# This iteratively removes the nodes from S with maximum connectivity to other
# set G\S. The first removal is arbitrary, as the other set it empty. You can
# see the first handful of iterations, all nodes in S are only connected to 1 in
# the other set.

S = set(G)
for _ in range(5):
    S.remove(max(S, key=count))
    print(sorted((count(v), v) for v in S if count(v) > 0))
