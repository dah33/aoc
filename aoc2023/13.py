def is_mirrored(rows, at):  # at is the first in 2nd side, so minimum is 1
    return all(t1 == t2 for t1, t2 in zip(rows[at - 1 :: -1], rows[at::1]))


def flip(image):
    return ["".join(row[i] for row in image) for i in range(len(image[0]))]


def mirror_line(image):  # 0 if no mirror line, sum of loc if >1
    return sum(j * is_mirrored(image, j) for j in range(1, len(image)))


# part 1
images = [s.split("\n") for s in open("./13.txt").read().split("\n\n")]
score = 100 * sum(mirror_line(image) for image in images)
score += sum(mirror_line(flip(image)) for image in images)
print(score)


def count_mirrors(image):
    return sum(is_mirrored(image, j) for j in range(1, len(image)))


def delta(image, at):  # number of changes -> is_mirrored true
    diffs = lambda t1, t2: sum(c1 != c2 for c1, c2 in zip(t1, t2))
    return sum(diffs(t1, t2) for t1, t2 in zip(image[at - 1 :: -1], image[at::1]))


# part 2

# check only one perfect mirror line per image (delta = 0) and one blurred
# mirror line per image (delta = 1)
for image in images:
    flipped = flip(image)
    assert count_mirrors(image) + count_mirrors(flipped) == 1
    changes = sorted(
        [delta(img, j) for img in (image, flipped) for j in range(1, len(img))]
    )
    assert changes[0:2] == [0, 1]

score = 0
for image in images:
    flipped = flip(image)
    score += sum(
        j * mult
        for img, mult in ((image, 100), (flipped, 1))
        for j in range(1, len(img))
        if delta(img, j) == 1  # use 0 for part 1
    )
print(score)

# lessons:
# - flip and linear scoring are good tricks learned from previous comps
# - hypothesis unique delta = 0 and delta = 1 worth testing, but could be assumed for speed
