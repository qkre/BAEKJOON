# 마인크래프트
# 구현, 브루트포스
from sys import stdin

input = stdin.readline

N, M, B = map(int, input().split())
blocks = list(list(map(int, input().split())) for _ in range(N))

min_height = 256
max_height = 0

needed_block = 0

for block_col in blocks:
    min_height = min(min_height, min(block_col))
    max_height = max(max_height, max(block_col))

if max_height - min_height == 1:
    min_count = 0
    max_count = 0
    for block_col in blocks:
        min_count += block_col.count(min_height)
        max_count += block_col.count(max_height)

    if min_count > max_count:
        print(max_count * 2, min_height)
        quit()
    else:
        needed_block = min_count
else:
    mid_height = max_height + min_height // 2

    min_count = 0
    max_count = 0
    for block_col in blocks:
        min_count += block_col.count(min_height)
        max_count += block_col.count(max_count)

    if B >= min_count + max_count:
        print(max_count*2 + min_count, mid_height)
    else:
        
