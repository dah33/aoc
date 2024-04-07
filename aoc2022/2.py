decode = lambda c: "ABCXYZ".index(c) % 3
games = [(decode[l[0]], decode[l[2]]) for l in open("./2.txt")]

POINTS = [3, 0, 6]  # draw lose win
score = lambda p1, p2: POINTS[(p1 - p2) % 3] + p2 + 1
print(sum(score(p1, p2) for p1, p2 in games))

# g[0] is p1
# g[1] is r = lose, draw, win
p2 = lambda p1, r: (p1 - [1, 0, 2][r]) % 3
print(sum(score(p1, p2(p1, r)) for p1, r in games))
