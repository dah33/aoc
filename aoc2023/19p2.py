import re
from math import prod
from spans import intrange
from typing import Dict

MIN = 1
MAX = 4000


def rule_fn(defn):
    if ":" not in defn:
        return lambda part: (part, defn, None)  # map all to wf, no remainder
    var, cmp, val, to_name = re.match("(\w+)([<>])(\d+):(\w+)", defn).groups()
    val = int(val)
    if cmp == ">":
        r = intrange(val, MAX, lower_inc=False, upper_inc=True)
    else:
        r = intrange(MIN, val, lower_inc=True, upper_inc=False)

    def fn(xmas: Dict[str, intrange]) -> (intrange, str, intrange):
        x = xmas[var]
        if x.intersection(r):
            intersection = xmas.copy()
            intersection[var] = x.intersection(r)
        else:
            intersection = None
        if x.difference(r):
            remainder = xmas.copy()
            remainder[var] = x.difference(r)
        else:
            remainder = None
        return intersection, to_name, remainder

    return fn


def parse_wf(wf):
    from_name, rules = re.match("([a-z]+){(.*)}", wf).groups()
    rule_fns = [rule_fn(defn) for defn in rules.split(",")]
    return from_name, rule_fns


section1, section2 = open("./19.txt").read().split("\n\n")
wfs = dict(parse_wf(wf) for wf in section1.split("\n"))
parts = [dict(re.findall("(\w)=(\d+)", p)) for p in section2.split("\n")]
parts = [{k: intrange(int(v), int(v) + 1) for k, v in part.items()} for part in parts]

universe = dict(zip("xmas", [intrange(MIN, MAX + 1)] * 4))
todo = [(universe, "in")]
done = {"A": [], "R": []}
while todo:
    part, wf_name = todo.pop()
    wf = wfs[wf_name]
    for rule_fn in wf:
        intersection, to_name, part = rule_fn(part)
        if intersection:
            if to_name in "AR":
                done[to_name].append(intersection)
            else:
                todo.append((intersection, to_name))
        if not part:
            break

# part 2 - assume all ranges distinct
print(sum(prod(map(len, xmas.values())) for xmas in done["A"]))

# Lessons
# - 4HbQ code is inspiring, should always read it
# - we're just checking if a part is accepted
# - this is just a boolean calc based on the values of xmas
# - it's just that the boolean calc is very nested
# - i didn't spot the and/or part!
# - using exec to create the functions is clever, as once created they're quick
# - i don't understand 1 appears in the lambda below, possibly some bool trick?
# - the splits code is great. only need to check a single point inside a split

# 4HbQ extra code for part 2, again amazing:

flows, parts = open("19.txt").read().split("\n\n")

A_ = lambda: 1 + x + m + a + s  # for part 1, we sum the xmas values
R_ = lambda: 1
S_ = 0

exec(
    flows.replace(":", " and ")
    .replace(",", "_() or ")
    .replace("{", "_ = lambda: ")
    .replace("}", "_()")
)

exec(parts.replace(",", ";").replace("{", "").replace("}", ";S_+=in_()-1"))

# part 1
print(S_)

# extension for part 2
import re

splits = {c: [0, 4000] for c in "xmas"}

for c, o, v in re.findall(r"(\w+)(<|>)(\d+)", flows):
    splits[c].append(int(v) - (o == "<"))

ranges = lambda x: [(a, a - b) for a, b in zip(x[1:], x)]
X, M, A, S = [ranges(sorted(splits[x])) for x in splits]

C = 0
for x, dx in X:
    for m, dm in M:
        for a, da in A:
            for s, ds in S:
                C += dx * dm * da * ds * bool(in_() - 1)

print(C)
