oasis = [[int(i) for i in l.split()] for l in open("./9.txt")]


def pred(vals):
    if all(v == 0 for v in vals):
        return 0
    diff = [y - x for x, y in zip(vals, vals[1:])]
    return vals[-1] + pred(diff)


print(sum(pred(vals) for vals in oasis))
print(sum(pred(list(reversed(vals))) for vals in oasis))

# From solution megathread: since diff is linear we can sum all problems
vals = [sum(oasis[i][j] for i in range(len(oasis))) for j in range(len(oasis[0]))]
print(pred(vals))
print(pred(list(reversed(vals))))
