import sys

cells = {
    complex(i, j): c for j, r in enumerate(sys.stdin) for i, c in enumerate(r.strip())
}
visited = {}
beams = [(-1, 1)] # don't really like starting off the board
while beams:
    pos, dir = beams.pop()
    while dir not in visited.setdefault(pos, []):
        visited[pos].append(dir)
        pos += dir
        if pos not in cells:
            break
        c = cells[pos]
        rotated = 1j * dir.conjugate()
        if c == "|":
            dir = 1j
            beams.append((pos, -1j))
        elif c == "-":
            dir = 1
            beams.append((pos, -1))
        elif c == "/":
            dir = -rotated
        elif c == "\\":
            dir = rotated
print(len(visited) - 1)

# W = int(max(k.real for k in cells.keys())) + 1
# H = int(max(k.imag for k in cells.keys())) + 1
#
# for j in range(W):
#     for i in range(H):
#         k = complex(i, j)
#         c = cells[k]
#         if k in visited:
#             c = "#"
#         print(c, end="", sep="")
#     print()
