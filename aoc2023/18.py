from itertools import pairwise
from collections import Counter

DIR_MAP = {
    "U": complex(0, -1),
    "D": complex(0, 1),
    "L": complex(-1, 0),
    "R": complex(1, 0),
}

parse = lambda dir, steps, rgb: (DIR_MAP[dir], int(steps), rgb[2:-1])
plan = [parse(*l.split()) for l in open("./18.txt")]


def to_points(dirs, steps):
    pos = 0
    points = []
    for d, s in zip(dirs, steps):
        pos += s * d
        points.append(pos)
    return points


def shoelace_area(dirs, steps):
    points = to_points(dirs, steps)
    # inside area:
    area = 0.5 * sum(
        (a.imag + b.imag) * (a.real - b.real) for a, b in pairwise(points + points[:1])
    )
    # perimeter area
    area += 0.5 * sum(steps)
    # adjust for quarter square extra/less for right/left turns
    rl_counts = Counter(next / dir for dir, next in pairwise(dirs + dirs[:1]))
    area += 0.25 * (rl_counts[1j] - rl_counts[-1j])
    return int(area)


# part 1
print(shoelace_area([d for d, _, _ in plan], [s for _, s, _ in plan]))

# part 2
print(
    shoelace_area(
        [1j ** (4 + int(rgb[-1])) for _, _, rgb in plan],
        [int(rgb[0:5], 16) for _, _, rgb in plan],
    )
)

# Lessons
# - Shoelace is clever, and I'm getting a feel for it
# - Lots of simplifications in forum solutions
#   - pairwise(points + points[:1]) not needed, as last dir is up and expression is zero for U/D
#   - to_points() can be inlined
#   - shoelace simplifies as 0.5(x1 + x2)(y1-y2) is zero for horizontals, and +/-x1 for U/D
#   - perimeter adjustment is always 1 for clockwise drawing, and indeed for counterclockwise

def shoelace_area_v2(dirs, steps):
    pos = 0
    prev_x = 0
    area = 0
    for d, s in zip(dirs, steps):
        pos += s * d
        area += pos.imag * (prev_x - pos.real)
        prev_x = pos.real
    area += sum(steps)//2 + 1
    return int(area)

# part 1
print(shoelace_area_v2([d for d, _, _ in plan], [s for _, s, _ in plan]))

# part 2
print(
    shoelace_area_v2(
        [1j ** (4 + int(rgb[-1])) for _, _, rgb in plan],
        [int(rgb[0:5], 16) for _, _, rgb in plan],
    )
)

# Lessons from 4HbQ
# - A joy to review!
# - Didn't use complex numbers here, unpacking in for loop is cool!
# - map string -> vector for both RDLU and 0123 is clever
# - using ans=1 as arg, with perimeter correction built in, v neat
# - they've further simplified shoelace, which makes my brain hurt!
#
# plan = list(map(str.split, open('data.txt')))
#
# dirs = {'R': (1,0), 'D': (0,1), 'L': (-1,0), 'U': (0,-1),
#         '0': (1,0), '1': (0,1), '2': (-1,0), '3': (0,-1)}
#
# def f(steps, pos=0, ans=1):
#     for (x,y), n in steps:
#         pos += x*n
#         ans += y*n * pos + n/2
#
#     return int(ans)
#
# print(f((dirs[d],    int(s))          for d,s,_ in plan),
#       f((dirs[c[7]], int(c[2:7], 16)) for _,_,c in plan))