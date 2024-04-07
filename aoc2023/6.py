from math import prod, sqrt, floor, ceil

# part 1 - brute force
records = (34, 204), (90, 1713), (89, 1210), (86, 1780)
prod(sum((t - p) * p > d for p in range(1, t - 1)) for t, d in records)

# part 2 - find integers strictly inside quadratic solution
t, d = 34908986, 204171312101780
real_sols = [(t + sign * sqrt(t * t - 4 * d)) / 2 for sign in [-1, 1]]
int_sols = range(floor(real_sols[0]) + 1, ceil(real_sols[1]))
len(int_sols)
