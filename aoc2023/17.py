import heapq
import itertools

losses = {
    (i, j): int(c)
    for j, r in enumerate(open("./17.txt"))
    for i, c in enumerate(r.strip())
}
coords = losses.keys()
W = max(i for i, _ in coords) + 1
H = max(j for _, j in coords) + 1
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
next_dirs = {
    (1, 0): ((1, 0), (0, -1), (0, 1)),
    (-1, 0): ((-1, 0), (0, 1), (0, -1)),
    (0, 1): ((0, 1), (1, 0), (-1, 0)),
    (0, -1): ((0, -1), (-1, 0), (1, 0)),
}
MIN_COUNT = 4
MAX_COUNT = 10
counters = list(range(1, MAX_COUNT + 1))
INF = float("inf")


def V():  # overgenerates, e.g. not possible to arrive up on the lower edge
    return itertools.product(coords, dirs, counters)


def w(_, v):
    return losses[v[0]]  # only v.pos is required


def neighbours(u):
    pos, dir, counter = u
    if counter == 0:  # special case, starting position
        valid_dirs = next_dirs[dir]  # free choice
    elif counter < MIN_COUNT:
        valid_dirs = next_dirs[dir][0:1]  # must continue
    elif counter >= MAX_COUNT:
        valid_dirs = next_dirs[dir][1:]  # must turn
    else:
        valid_dirs = next_dirs[dir]  # free choice
    return [
        ((pos[0] + d[0], pos[1] + d[1]), d, counter + 1 if d == dir else 1)
        for d in valid_dirs
        if (pos[0] + d[0], pos[1] + d[1]) in coords
    ]


def dijkstra(s):
    """
    Dijsktra's algorithm for a heap that does not support decrease_priority()
    Ref: https://www3.cs.stonybrook.edu/~rezaul/papers/TR-07-54.pdf
    """
    Q = []
    dist = {v: INF for v in V()}
    dist[s] = 0
    heapq.heappush(Q, (dist[s], *s))  # unnest s for readability
    prev = {}
    while Q:
        k, *u = heapq.heappop(Q)
        u = tuple(u)
        if k > dist[u]:
            continue  # already "removed" from priority queue
        for v in neighbours(u):
            alt_dist = dist[u] + w(u, v)
            if alt_dist < dist[v]:  # also no need if dist lower for a lower counter
                heapq.heappush(Q, (alt_dist, *v))
                dist[v] = alt_dist
                prev[v] = u
    return dist, prev


def astar(source, target_pos):
    """
    A* algorithm for a heap that does not support decrease_priority()
    Derived from Djikstra's algorithm above.
    """
    Q = []
    h = lambda v: sum(abs(v[0][i] - target_pos[i]) for i in range(2))
    g = {v: INF for v in V()}  # from source to v
    g[source] = 0
    f = {v: INF for v in V()}  # from source to target via v
    f[source] = h(source)
    prev = {}
    heapq.heappush(Q, (0, *source))
    while Q:
        k, *u = heapq.heappop(Q)
        u = tuple(u)
        if k > g[u] + h(u):
            continue  # "removed" from priority queue
        for v in neighbours(u):
            g_tentative = g[u] + w(u, v)
            if g_tentative < g[v]:  # also no need if dist lower for a lower counter
                g[v] = g_tentative  # shortest distance (so far) to v
                f[v] = g[v] + h(v)  # est. of shortest dist to target via v
                heapq.heappush(Q, (f[v], *v))
                prev[v] = u
    return g, prev


def show(prev, source, target):
    v = target
    route = {}
    while v != source:
        route[v[0]] = v[1]
        v = prev[v]
    for j in range(H):
        for i in range(W):
            k = (i, j)
            match route.get(k):
                case (1, 0):
                    c = ">"
                case (-1, 0):
                    c = "<"
                case (0, 1):
                    c = "v"
                case (0, -1):
                    c = "^"
                case None:
                    c = losses[k]
            print(c, end="", sep="")
        print()


source = (
    (0, 0),  # at origin
    (1, 0),  # got here going right
    0,  # counter of zero: not valid normally, but don't want to restrict
)
target_pos = (W - 1, H - 1)

# dist, prev = dijkstra(source)
dist, prev = astar(source, target_pos)

# Many ways to get to target
valid_targets = [(target_pos, d, c) for d, c in itertools.product(dirs, counters)]
solutions = [(dist.get(v, INF), *v) for v in valid_targets]

# But which variant has the lowest heat loss?
heapq.heapify(solutions)
loss, *target_variant = heapq.heappop(solutions)
target_variant = tuple(target_variant)

print("Lowest loss is", loss, "ending at", target_variant)
show(prev, source, target_variant)

# Lessons:
# - My initial attempt was a depth first search, which explodes for the test case
# - You need to use heuristics to prioritise the most likely path
# - Learned about dijkstra and other shortest path algorithms
# - Dijkstra prioritises (shortest path) to closest points to start
# - A* adds an estimate of the remaining distance
# - Complex numbers trick complicated matters given I didn't know the algorithm
# - NetworkX looks interesting, but need to be careful which edges I generate
# - Learned about priority queues, and heapq
# - Heapq doesn't have reduce priority, but it's easier to vary the algorith to ignore deleted keys

# 4HbQ solution is very smart (as always)
# - when you generate the next step, you can do all the steps from min to max
#   allowed, and quickly add up the lengths of each
# - using complex numbers makes this easy, as you can easily say 3 steps right =
#   3*dir
# - he doesn't go straight. instead he goes left or right from current
#   direction, until next turn, at which point left or right again

# Doesn't quite work, as V() overgenerates, e.g. coming upwards from the lower edge.
#
# import networkx as nx
#
# G = nx.Graph()
# G.add_nodes_from(V())
# G.add_node(source)
# G.add_edges_from([(u, v) for u in G.nodes for v in neighbours(u)])
# weight_fn = lambda u, v, _: w(u, v)
# path_lengths, paths = nx.single_source_dijkstra(G, source, weight=weight_fn)
# solutions = sorted([(path_lengths[p], p) for p in valid_targets])
# loss, target_variant = solutions[0]
# print("Lowest loss is", loss, "ending at", target_variant)
# show(prev, source, target_variant)
