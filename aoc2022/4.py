import re

# With sets using pairs
elf_pairs = [re.findall("(\d+)-(\d+)", l) for l in open("./4.txt")]
to_set = lambda p: set(range(int(p[0]), int(p[1]) + 1))

fully_contained = lambda p: len(to_set(p[0]).intersection(to_set(p[1]))) == min(
    len(to_set(p[0])), len(to_set(p[1]))
)
print(len([p for p in elf_pairs if fully_contained(p)]))

overlapping = lambda p: len(to_set(p[0]).intersection(to_set(p[1])))
print(len([p for p in elf_pairs if overlapping(p)]))

# With range tests on p[0..4]
elf_pairs = [tuple(map(int, re.findall("(\d+)", l))) for l in open("./4.txt")]

fully_contained = lambda p: (p[0] <= p[2] and p[1] >= p[3]) or (
    p[0] >= p[2] and p[1] <= p[3]
)
print(len([p for p in elf_pairs if fully_contained(p)]))

overlapping = lambda p: p[0] <= p[3] and p[2] <= p[1]
print(len([p for p in elf_pairs if overlapping(p)]))

# With lessons:
# * Simplest parsing makes type conversion easier
# * Pre-prepare logic for range detection:
elf_pairs = [tuple(map(int, re.findall("(\d+)", l))) for l in open("./4.txt")]

# Defined in utils.py:
fully_contained = lambda x, y, a, b: (x <= a and y >= b) or (x >= a and y <= b)
overlapping = lambda x, y, a, b: x <= b and a <= y # both left and right overlap

print(len([p for p in elf_pairs if fully_contained(*p)]))
print(len([p for p in elf_pairs if overlapping(*p)]))
