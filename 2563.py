import math

N = int(input())
nums = []
min_X, min_Y = 0, 0
max_X, max_Y = 0, 0
for i in range(N):
    nums.append(list(map(int, input().split())))
    if i == 0:
        min_X, min_Y = nums[0][0], nums[0][1]
        max_X, max_Y = nums[0][0], nums[0][1]
    else:
        min_X, min_Y = min(min_X, nums[i][0]), min(min_Y, nums[i][1])
        max_X, max_Y = max(max_X, nums[i][0]), max(max_Y, nums[i][1])

w, h = max_X - min_X, max_Y - min_Y

area = [[0] * (w + 10) for _ in range(h + 10)]

for x, y in nums:
    x -= min_X
    y -= min_Y

    for i in range(10):
        for j in range(10):
            area[y + j][x + i] = 1

result = 0
for col in area:
    result += col.count(1)

print(result)
