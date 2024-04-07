from functools import reduce

sacks = [
    (l[: len(l) // 2], l[len(l) // 2 : -1])
    for l in open(
        "./3.txt",
    )
]
common = lambda s1, s2: set(s1).intersection(set(s2))
priority = lambda c: ord(c) - ord("a") + 1 if c >= "a" else ord(c) - ord("A") + 27
first = lambda s: list(s)[0]
print(sum([priority(first(common(s1, s2))) for s1, s2 in sacks]))

chunk = lambda l, n: [l[i : i + n] for i in range(0, len(l), n)]
groups = chunk(list(map(lambda s: s.rstrip(), open("./3.txt"))), 3)
print(sum(priority(first(reduce(common, g))) for g in groups))
