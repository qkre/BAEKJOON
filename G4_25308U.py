from sys import stdin

input = stdin.readline

import itertools

positions = list(map(int, input().split()))
permutations = list(itertools.permutations(positions))
count = 0
for permutation in permutations:
    if permutation[1] ** 2 < permutation[0] ** 2 + permutation[2] ** 2:
        continue
    if permutation[3] ** 2 < permutation[2] ** 2 + permutation[4] ** 2:
        continue
    if permutation[5] ** 2 < permutation[4] ** 2 + permutation[6] ** 2:
        continue
    if permutation[7] ** 2 < permutation[0] ** 2 + permutation[6] ** 2:
        continue

    count += 1

print(count)
