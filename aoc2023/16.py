import sys

sys.setrecursionlimit(10_000)

STEP = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}

def reflect(p, dir):
    match p:
        case "\\":
            return dir.translate(str.maketrans("^v<>", "<>^v"))
        case "/":
            return dir.translate(str.maketrans("^v<>", "><v^"))
        case "|":
            return dir if dir in "^v" else "^v"
        case "-":
            return dir if dir in "<>" else "<>"
        case _:
            return dir


def beam(rows, i, j, dir, visited=None):
    if visited is None:
        visited = dict()
    if i < 0 or j < 0 or i >= len(rows[0]) or j >= len(rows):
        return visited
    if (i, j) in visited and dir in visited[(i, j)]:
        return visited
    visited[i, j] = visited.get((i, j), "") + dir
    p = rows[j][i]
    for new_dir in reflect(p, dir):
        di, dj = STEP[new_dir]
        visited = beam(rows, i + di, j + dj, new_dir, visited)
    return visited


def show(rows, visited):
    for j, r in enumerate(rows):
        for i, c in enumerate(r):
            if (i, j) in visited:
                c = "#"
            print(c, end="", sep="")
        print()


def beam_length(rows, i, j, dir):
    visited = beam(rows, i, j, dir)
    return len(visited)


rows = [l.strip() for l in open("./16.txt")]

# part 1
visited = beam(rows, 0, 0, ">")
show(rows, visited)
print(len(visited))

# part 2
max_beam = 0
for j in range(len(rows)):
    max_beam = max(max_beam, beam_length(rows, 0, j, ">"))
    max_beam = max(max_beam, beam_length(rows, len(rows[j]) - 1, j, "<"))
for i in range(len(rows[0])):
    max_beam = max(max_beam, beam_length(rows, i, 0, "v"))
    max_beam = max(max_beam, beam_length(rows, i, len(rows) - 1, "^"))
print(max_beam)
