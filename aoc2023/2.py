import re, math

BAG, RGB = [12, 13, 14], ["red", "green", "blue"]
parse = lambda l: [max(int(s) for s in re.findall(f"(\d+) {c}", l)) for c in RGB]
games = list(map(parse, open("./2.txt")))

is_possible = lambda game: all(c <= m for c, m in zip(game, BAG))
print(
    sum(i + 1 for i, game in enumerate(games) if is_possible(game)),
    "games possible with bag",
    [f"{b} {c}" for b, c in zip(BAG, RGB)],
)

print("Combined power is", sum(math.prod(g) for g in games))
