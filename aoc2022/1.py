cal = [sum(map(int, e.split("\n"))) for e in open("1.txt").read().split("\n\n")]
print(max(cal))
print(sum(sorted(cal)[-3:]))
