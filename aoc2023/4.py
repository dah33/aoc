import re

cards = [re.findall("(\d+)", l)[1:] for l in open("./4.txt")]
N = 10  # 5 for test examples
winning = [set(c[:N]) for c in cards]
numbers = [set(c[N:]) for c in cards]
matches = [len(n.intersection(w)) for n, w in zip(numbers, winning)]
print(sum(2 ** (m - 1) for m in matches if m > 0))
acc = [1] * len(cards)
for i, m in enumerate(matches):
    for d in range(m):
        j = i + 1 + d
        if j < len(matches):
            acc[j] += acc[i]
print(sum(acc))
