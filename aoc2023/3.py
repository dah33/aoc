import re

grid = [l.rstrip() for l in open("./3.txt")]
mask = [re.sub("\d", ".", l) for l in grid]


def part_nearby(r, c):
    global mask
    for row in mask[max(r - 1, 0) : min(r + 2, len(mask))]:
        if row[max(c - 1, 0) : min(c + 2, len(mask[0]))].strip(".") != "":
            return True
    return False


acc = 0
for r, row in enumerate(grid):
    part_num, nearby = 0, False
    for c, cell in enumerate(row + "."):  # ensures part_num ends
        if cell.isdigit():
            part_num = part_num * 10 + int(cell)
            nearby = nearby or part_nearby(r, c)
        else:
            if part_num and nearby:
                # print("found number", part_num)
                acc += part_num
            part_num, nearby = 0, False
print(acc)  # 512794


def nearby_gears(r, c):
    global mask
    gear_locs = set()
    for y in range(max(r - 1, 0), min(r + 2, len(mask))):
        for x in range(max(c - 1, 0), min(c + 2, len(mask[0]))):
            if mask[y][x] == "*":
                gear_locs.add((y, x))
    return gear_locs


print(nearby_gears(3, 2))

gears = {}
for r, row in enumerate(grid):
    part_num, nearby = 0, set()
    for c, cell in enumerate(row + "."):  # ensures part_num ends
        if cell.isdigit():
            part_num = part_num * 10 + int(cell)
            nearby = nearby.union(nearby_gears(r, c))
        else:
            if part_num and nearby:
                # print("found number", part_num, "near gears", nearby)
                for gear_loc in nearby:
                    gears[gear_loc] = gears.get(gear_loc, []) + [part_num]
            part_num, nearby = 0, set()
print(
    sum(
        part_nums[0] * part_nums[1]
        for part_nums in gears.values()
        if len(part_nums) == 2
    )
)

# Lesson? Not much. Seems nasty!
