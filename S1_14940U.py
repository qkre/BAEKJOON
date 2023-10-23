from sys import stdin

input = stdin.readline

global mini_map, cost, N, M, visited, destX, destY

N, M = map(int, input().split())


mini_map = list(list(map(int, input().split())) for _ in range(N))
cost = list(list(0 for _ in range(M)) for _ in range(N))
visited = list(list(False for _ in range(M)) for _ in range(N))

destX, destY = 0, 0
for y in range(N):
    for x in range(M):
        if mini_map[y][x] == 2:
            destX = x
            destY = y
            break

# 목적지 기준 1사분면
startX, startY = M - 1, 0

for y in range(destY):
    cost[y][startX] = y
    for x in range(startX, destX - 1, -1):
        cost[0][x] = startX - x


# 목적지 기준 2사분면
startX, startY = 0, 0

for y in range(destY):
    cost[y][0] = y
    for x in range(destX):
        cost[0][x] = x

for y in range(1, destY):
    for x in range(1, destX):
        cost[y][x] = cost[y - 1][x] + cost[y][x - 1] - cost[y - 1][x - 1]


# 목적지 기준 3사분면
startX, startY = 0, N - 1


# 목적지 기준 4사분면
startX, startY = M - 1, N - 1
