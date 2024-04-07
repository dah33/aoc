import re

from itertools import product, pairwise

det = lambda a, b: a[0] * b[1] - a[1] * b[0]
add = lambda a, b: (a[0] + b[0], a[1] + b[1])
sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
mul = lambda s, v: (s * v[0], s * v[1])

paths = [list(map(int, re.findall("-?\d+", l))) for l in open("./24.txt")]
paths = [(p[:3], p[3:]) for p in paths]


# From: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def intersect_time(A, V, B, W):
    div = det(V, W)
    if div == 0:
        return None, None, None
    AB = sub(B, A)
    t = det(AB, W) / div
    u = det(AB, V) / div
    return t, u, add(A, mul(t, V))


# example - did on paper, check the rock is correct:
if len(paths) == 5:
    rock = (24, 13, 10, -3, 1, 2)
    B, W = rock[:3], rock[3:]
    for A, V in paths:
        t, u, P = intersect_time(A, V, B, W)
        print(A, B, t, u, P)
    exit(1)


r = range(-500, 500)
for V in product(r, r):
    intersect = None
    adj_paths = pairwise((B, sub(W, V)) for B, W in paths)
    for P1, P2 in adj_paths:
        t, u, x = intersect_time(*P1, *P2)
        if t is None:
            # P2 moving parallel to P1, so since P1 already checked against
            # previous, P2 will have a solution, possibly in the past, but we
            # can live with the false positive, as there's many other checks
            continue
        if t < 0 or u < 0:
            break
        if intersect and intersect != x:
            break
        intersect = x
    else:
        print("Velocity:", V)
        print("Intersect in 2D:", intersect)
        break

# This is a 2D intercept, so we solve for z

# Calculate hail intersect times and z pos
times = [(intersect[0] - B[0]) / sub(W, V)[0] for B, W in paths]
Zs = [B[2] + t * W[2] for (B, W), t in zip(paths, times)]

# Take first two z and calculate rock's z-speed
Zspeed = (Zs[0] - Zs[1]) / (times[0] - times[1])
Zstart = Zs[0] - times[0] * Zspeed

# Now we've got a 3D intercept!
i3d = tuple(map(int, (*intersect, Zstart)))
print("Intersect in 3D:", i3d)
print(sum(i3d))

# Lessons/Comments:
#
# I couldn't do this without hints!
# - First I tried to solve on paper, but the first example is chosen to be easy
#   to solve, and it's also very hard to keep track of the long numbers.
# - I thought about fixing the first hail at the origin, to simplify the math,
#   but still too hard for paper.
# - I also tried to write a guassian eliminator, but the algebra is too
#   complicated beyond the toy example.
# - It's some comfort I guess that posts on the forum say this is one of the
#   hardest problems for a few years!
#
# The hints say brute force!
# - The rock velocity is low and integers, so just try all low values.
# - Subtract the rock velocity from the hails' then see if they all intersect at
#   some point in the future. This would be the point to throw from. This reuses
#   the code from part 1, so seems to be the intended approach.
#
# Other ideas people had:
# - Some used solvers on the system of equations, e.g. Z3 library
# - Modulo trick:
#
#   What a weird solution for part 2 - I don't even have code to show for it
#   really. I didn't form a system of equations or use Z3 or anything, as it
#   seems most people did (I have no clue how to use Z3 in C++ code). Instead, I
#   did a little math and noticed that for any two hailstones with the same vx
#   value, the difference between that vx and the starting rock's x velocity
#   must be a divisor of the difference between the two x coordinates of those
#   hailstones. So I just wrote up a few lines of code that printed out the
#   prime factorizations of the differences between x coordinates for every pair
#   of hailstones with identical vx value. After staring at these prime
#   factorizations for a few minutes, there was a clear pattern: 99 - vx was
#   always present in the factorization, for every single pair. Thus I concluded
#   that the x velocity of the starting rock must be 99. I then repeated this
#   exact thing for the y and z coordinates, getting a starting velocity of (99,
#   240, 188).
