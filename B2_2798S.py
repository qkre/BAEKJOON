import itertools

N, M = map(int, input().split())

cards = list(map(int, input().split()))

combinations = list(itertools.combinations(cards, 3))

# combinations = list(map(sum, combinations))
# max_sum = 0
# for s in combinations:
#     if s <= M:
#         max_sum = max(max_sum, s)

# print(max_sum)

print(max((s for s in map(sum, combinations) if s <= M)))
