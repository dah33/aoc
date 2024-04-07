boxes = [{} for _ in range(256)]
for string in input().split(","):
    insert = string.strip("-").split("=")
    name = insert.pop(0)
    hash = 0
    for s in name:
        hash += ord(s)
        hash *= 17
        hash %= 256
    if insert:
        boxes[hash][name] = int(insert[0])
    else:
        boxes[hash].pop(name, 0)
print(
    sum(
        box * slot * focal
        for box, lenses in enumerate(boxes, 1)
        for slot, focal in enumerate(lenses.values(), 1)
    )
)
