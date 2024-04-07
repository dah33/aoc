STEP = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}
NEXT_DIR = {
    "^": str.maketrans("│╭╮", "^><"),
    "v": str.maketrans("│╰╯", "v><"),
    ">": str.maketrans("╯╮─", "^v>"),
    "<": str.maketrans("╰╭─", "^v<"),
}


def walk(rows, i, j, dir):
    """Return number of steps to start, or zero if not a loop."""
    steps = 0
    visited = set()
    is_cycle = False

    while i >= 0 and j >= 0 and i < len(rows[0]) and j < len(rows):
        steps += 1
        visited.add((i, j))
        p = rows[j][i]
        if p == "S":
            is_cycle = True
            break
        dir = str.translate(p, NEXT_DIR[dir])
        if dir not in "^v><":
            break
        di, dj = STEP[dir]
        i, j = i + di, j + dj

    return steps * is_cycle, visited


def parse_row(s):
    return list(s.rstrip().translate(str.maketrans("|-LJ7F", "│─╰╯╮╭")))


def show(rows):
    for r in rows:
        print("".join(str(c) for c in r))


# part 1
rows = [parse_row(row) for row in open("./10.txt")]
Si, Sj = [(i, j) for j, r in enumerate(rows) for i, c in enumerate(r) if c == "S"][0]
steps = 0
visited = None
for dir, (di, dj) in STEP.items():
    s, v = walk(rows, Si + di, Sj + dj, dir)
    if s > steps:
        steps = s
        visited = v

show(rows)
assert steps % 2 == 0
print(steps // 2)

# part 2 - painters algorithm for area
# assume scanline runs in top half of cells, so ╯╰ cross but not ╮╭
# assume S is not a crossing, which is true in the data: ╮
rows = [parse_row(row) for row in open("./10.txt")]
area = 0
for j, row in enumerate(rows):
    inside = False
    for i, p in enumerate(row):
        if (i, j) in visited:
            if p in "│╯╰":
                inside = not inside
        else:
            rows[j][i] = "I" if inside else "O"
            area += inside
show(rows)
print(area)
