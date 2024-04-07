def hash(s):
    h = 0
    for c in s:
        h = (h + ord(c)) * 17 % 256
    return h


# part 1
input = open("./15.txt").read().split(",")
print("part 1", sum(hash(s) for s in input))


# part 2 - allez cuisine (no libs)
def parse(s):
    if s[-1] == "-":
        return s[:-1], "-", None
    else:
        return s.split("=")[0], "=", int(s.split("=")[1])


procs = [parse(s) for s in open("./15.txt").read().split(",")]

hashmap = [{} for _ in range(256)]
for name, op, focal in procs:
    box = hash(name)
    lenses = hashmap[box]
    if op == "=":
        lens = (name, focal)
        lenses[name] = focal
    elif name in lenses:  # op = "-"
        del lenses[name]


def show(hashmap):
    for box, lenses in enumerate(hashmap):
        print(box, lenses)


def score(lenses):
    return sum((slot + 1) * focal for slot, focal in enumerate(lenses.values()))


print("part 2", sum((box + 1) * score(lenses) for box, lenses in enumerate(hashmap)))


# lessons
# - dict ops: del and replace if exists preserves order
# - match statement is nice


def megathread_solution():
    from functools import reduce

    data = open("15.txt").read().strip().split(",")

    char = lambda i, c: (i + ord(c)) * 17 % 256
    hash = lambda s: reduce(char, s, 0)

    print(sum(map(hash, data)))

    boxes = [dict() for _ in range(256)]

    # this is nice, parsing and conversion while reading
    # also hash inline and
    for step in data:
        match step.strip("-").split("="):  # strip and split is very nice!
            case [l, f]:
                boxes[hash(l)][l] = int(f)  # use name only as key
            case [l]:
                boxes[hash(l)].pop(l, 0)  # dict.pop with default
    print(boxes)
    print(
        sum(
            i * j * f
            for i, b in enumerate(boxes, 1)
            for j, f in enumerate(b.values(), 1)
        )
    )


megathread_solution()
