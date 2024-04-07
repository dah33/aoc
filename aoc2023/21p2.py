import math

grid = [l.rstrip("\n") for l in open("./21.txt")]

S = [(row.find("S"), j) for j, row in enumerate(grid) if "S" in row][0]
Si, Sj = S
grid[Sj] = grid[Sj][:Si] + "." + grid[Sj][Si + 1 :]
W = len(grid[0])
H = len(grid)

# note that n = 26501365 % 131 (the W/H) = 65, so just solve for n = 65
# then repeat the patterns found
# looked at the diamond overlaying a grid, forming tiles, and realised the
# total count would be a quadratic combination of areas of each tile choice
# so can just work out coeffcients of the quadratic


def walk(n=65):
    m = int(math.ceil((2* n + 1) / 131))
    g = [row * m for row in grid] * m
    s = S[0] + m // 2 * W, S[1] + m // 2 * H
    todo = {s}
    valid = set((i, j) for i in range(W * m) for j in range(H * m))
    for _ in range(n):
        done = set()
        while todo:
            pos = todo.pop()
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                p2 = pos[0] + dir[0], pos[1] + dir[1]
                if p2 not in done and p2 in valid and g[p2[1]][p2[0]] == ".":
                    done.add(p2)
        todo = done
    return len(todo)


for k in list(range(3)):
    n = 131 * (k * 2) + 65
    m = 2 * (k * 2) + 1
    print(k, walk(n, m))

# fit quadratic: ak2 + bk + c = walk(k)
# k = 0, walk = 3784 => c = 3784
# k = 1, walk = 93366 => a + b + c = 93366 => a + b = 89582
# k = 2, walk = 302108 => 4a + 2b + c = 302108 => 2a + b = 149162
# => a = 59580
# => b = -30002

f = lambda k: 59580 * k * k + 30002 * k + 3784
f(4)  # 1077072

# confirm with test
k = 4
n = 131 * (k * 2) + 65
m = 2 * (k * 2) + 1
print(k, walk(n, m))
# 4 1077072 -- correct!

N = 26501365
assert (N - 65) % 131 == 0
assert (N - 65) // 131 % 2 == 0
K = (N - 65) // 131 / 2  # cycles
f(K)  # 609_585_229_256_084
