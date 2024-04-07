import functools
import time


def parse(line):
    springs, runs = line.split()
    runs = tuple(int(n) for n in runs.split(","))
    return springs, runs


@functools.cache
def ways(row, runs, run_len=0):
    if not runs:
        return 0 if "#" in row else 1
    next_run = runs[0]
    if run_len > next_run:
        return 0
    if row == "":
        return len(runs) == 1 and run_len == next_run
    c, row = row[0], row[1:]
    if c == ".":
        if run_len:
            if run_len != next_run:
                return 0
            runs = runs[1:]
        return ways(row, runs, 0)
    elif c == "#":
        return ways(row, runs, run_len + 1)
    else:  # c == "?"
        return sum(ways(s + row, runs, run_len) for s in "#.")


data = [parse(line) for line in open("./12.txt")]


t0 = time.time()
print(sum(ways(row, runs) for row, runs in data))
print(sum(ways("?".join([row] * 5), runs * 5) for row, runs in data))
print(time.time() - t0)

# lessons
# - should start with cache, and avoid trying to optimise the flow
# - start recursion function with base cases
# - branch with return, make all branches have a return, and ensure there's else
# - "ways" is a nice short name for permutations/arrangements
