# grid = [l.rstrip("\n") for l in open("./21.txt")]
# start = [(row.find("S"), j) for j, row in enumerate(grid) if "S" in row][0]


def show(locations):
    for j in range(W):
        for i in range(H):
            pos = complex(i, j)
            c = grid[pos]
            if complex(i, j) in locations:
                c = "O"
            print(c, sep="", end="")
        print()


grid = {
    complex(i, j): c
    for j, l in enumerate(open("./21.txt"))
    for i, c in enumerate(l.strip("\n"))
}
S = [k for k, v in grid.items() if v == "S"][0]
grid[S] = "."
W = int(max(pos.real for pos in grid)) + 1
H = int(max(pos.imag for pos in grid)) + 1

n = 64
todo = {S}
for i in range(n):
    done = set()
    while todo:
        pos = todo.pop()
        for dir in [1, -1, 1j, -1j]:
            p2 = pos + dir
            if p2 not in done and p2 in grid and grid[p2] == ".":
                done.add(p2)
    todo = done
print(todo)
show(todo)
print(len(todo))
