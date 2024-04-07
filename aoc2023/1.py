import re

for words in [[], "zero one two three four five six seven eight nine".split()]:
    to_int = lambda s: int(s) if s.isdigit() else words.index(s)
    pattern = "(?=(" + "|".join(["\d"] + words) + "))"  # finds overlapping
    dd = [[to_int(d) for d in re.findall(pattern, s)] for s in open("./1.txt")]

    print(sum([10 * d[0] + d[-1] for d in dd]))
