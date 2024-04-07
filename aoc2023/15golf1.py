total = 0
for string in input().split(","):
    val = 0
    for s in string:
        val += ord(s)
        val *= 17
        val %= 256
    total += val
print(total)