import re
from spans import intrange, intrangeset


def parse_maps(lines, make_map) -> list[list[callable]]:
    maplists, maplist = [], []
    for line in list(lines) + [""]:
        if len(line) and line[0].isdigit():
            ds, ss, n = list(map(int, re.findall("(\d+)", line)))
            maplist.append(make_map(ds, ss, n))
        elif len(maplist):
            maplists.append(maplist)
            maplist = []
    return maplists


def make_intrange_map(ds: int, ss: int, n: int) -> callable:
    def my_map(r: intrange):
        s = intrange(ss, ss + n)
        if r.overlap(s):
            mapped = r.intersection(s).offset(ds - ss)
            unmapped = intrangeset([r]).difference(intrangeset([s]))
        else:
            mapped = None
            unmapped = intrangeset([r])
        return mapped, unmapped

    return my_map


def apply_maps(maplist, inputs):
    mapped = []
    for m in maplist:
        residuals = []
        for i in inputs:
            i_mapped, i_residuals = m(i)
            if i_mapped:
                mapped.append(i_mapped)
            residuals.extend(i_residuals)
        inputs = residuals
    mapped.extend(residuals)
    return mapped


lines = list(open("./5.txt"))
raw_seeds = list(map(int, re.findall("(\d+)", lines.pop(0))))

seed_ints = [intrange(x, x + 1) for x in raw_seeds]
seed_ranges = [intrange(x, x + n) for x, n in zip(raw_seeds[0::2], raw_seeds[1::2])]

for seeds in [seed_ints, seed_ranges]:
    for maplist in parse_maps(lines, make_intrange_map):
        seeds = apply_maps(maplist, seeds)
    print(min(s.lower for s in seeds))
