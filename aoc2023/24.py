import re
from itertools import combinations


# From: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def intersect_time(A, V, B, W):
    det = lambda a, b: a[0] * b[1] - a[1] * b[0]
    add = lambda a, b: (a[0] + b[0], a[1] + b[1])
    sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
    mul = lambda s, v: (s * v[0], s * v[1])
    div = det(V, W)
    if div == 0:
        return None, None, None
    AB = sub(B, A)
    t = det(AB, W) / div
    u = det(AB, V) / div
    return t, u, add(A, mul(t, V))


paths = [list(map(int, re.findall("-?\d+", l))) for l in open("./24.txt")]
paths = [(p[:3], p[3:]) for p in paths]
BOUNDS = ((7, 27),) * 3 if len(paths) == 5 else ((2e14, 4e14),) * 3

n = 0
for path1, path2 in combinations(paths, 2):
    A, V = path1
    B, W = path2
    t, u, P = intersect_time(A, V, B, W)
    if (
        t
        and t > 0
        and u > 0
        and P[0] >= BOUNDS[0][0]
        and P[0] <= BOUNDS[0][1]
        and P[1] >= BOUNDS[1][0]
        and P[1] <= BOUNDS[1][1]
    ):
        print(A, B, t, u, P)
        n += 1
print(n)

