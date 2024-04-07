trail = {
    (i, j): c
    for j, line in enumerate(open("./23.txt"))
    for i, c in enumerate(line.strip())
}

STEPS = (1, 0), (-1, 0), (0, 1), (0, -1)
W = max(i for i, _ in trail) + 1
H = max(j for _, j in trail) + 1
start = min(pos[0] for pos in trail if pos[1] == 0 and trail[pos] == ".")
end = min(pos[0] for pos in trail if pos[1] == H - 1 and trail[pos] == ".")
start = (start, 0)
end = (end, H - 1)

# part 1
todo = [(start, set())]  # pos, path so far
done = []
while todo:
    u, path = todo.pop()
    match trail[u]:
        case ">":
            dirs = [(1, 0)]
        case "<":
            dirs = [(-1, 0)]
        case "^":
            dirs = [(0, -1)]
        case "v":
            dirs = [(0, 1)]
        case _:
            dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    for s in dirs:
        v = u[0] + s[0], u[1] + s[1]
        if trail.get(v, "#") != "#" and v not in path:
            if v == end:
                done.append(path | {v})
            todo.append((v, path | {v}))

print(max(len(path) for path in done))

# Visualise path
max_len, path = sorted((len(path), path) for path in done)[0]
for j, line in enumerate(open("./23.txt")):
    for i, c in enumerate(line.strip()):
        if (i, j) in path:
            c = "o"
        print(c, end="")
    print()
