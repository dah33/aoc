from itertools import accumulate, combinations

image = [l.rstrip() for l in open("./11.txt")]

H = len(image)
W = len(image[0])
gal = [(i, j) for j, row in enumerate(image) for i, c in enumerate(row) if c == "#"]
empty_rows = ["#" not in row for row in image]
empty_cols = [all(row[i] == "." for row in image) for i in range(W)]

# part 1
dx = list(accumulate(empty_cols, initial=0))
dy = list(accumulate(empty_rows, initial=0))
galx = [(i + dx[i], j + dy[j]) for i, j in gal]
print(sum(abs(i - x) + abs(y - j) for (i, j), (x, y) in combinations(galx, 2)))

# part 2
n = 1000_000
dx = list(accumulate((x * (n - 1) for x in empty_cols), initial=0))
dy = list(accumulate((x * (n - 1) for x in empty_rows), initial=0))
galx = [(i + dx[i], j + dy[j]) for i, j in gal]
print(sum(abs(i - x) + abs(y - j) for (i, j), (x, y) in combinations(galx, 2)))

# learnings
# - don't need combinations, just do over all pairs and divide by 2
# - can do x and y separately, then sum
