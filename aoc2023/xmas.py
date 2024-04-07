import itertools

f = "MERRYXMASTOALL"

len(set(f))
# 10


def is_correct(m):
    merry = m["M"] * 10_000 + m["E"] * 1_000 + m["R"] * (100 + 10) + m["Y"]
    xmas = m["X"] * 1_000 + m["M"] * 100 + m["A"] * 10 + m["S"]
    toall = m["T"] * 10_000 + m["O"] * 1000 + m["A"] * 100 + m["L"] * (10 + 1)
    return merry + xmas == toall


def toall(m):
    toall = m["T"] * 10_000 + m["O"] * 1000 + m["A"] * 100 + m["L"] * (10 + 1)
    return toall


for letters in itertools.permutations(set(f)):
    map = {letter: number for number, letter in enumerate(letters)}
    if is_correct(map):
        print(map)
        print("toall", toall(map))

# {'O': 0, 'S': 1, 'Y': 2, 'L': 3, 'E': 4, 'X': 5, 'A': 6, 'R': 7, 'M': 8, 'T': 9}
# toall 90633
# {'O': 0, 'S': 1, 'Y': 2, 'L': 3, 'X': 4, 'E': 5, 'A': 6, 'R': 7, 'M': 8, 'T': 9}
# toall 90633
# {'O': 0, 'Y': 1, 'S': 2, 'L': 3, 'E': 4, 'X': 5, 'A': 6, 'R': 7, 'M': 8, 'T': 9}
# toall 90633
# {'O': 0, 'Y': 1, 'S': 2, 'L': 3, 'X': 4, 'E': 5, 'A': 6, 'R': 7, 'M': 8, 'T': 9}
# toall 90633
