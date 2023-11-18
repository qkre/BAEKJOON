from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

arr = list(list(map(int, input().split())) for _ in range(N))

lands = 0

def bfs(s, e):
    global N
    q = deque()
    q.append((s, e))

    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and land[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True

    return True


for i in range(0, 100):

    land = list([False] * N for _ in range(N))
    visited = list([False] * N for _ in range(N))

    for y in range(N):
        for x in range(N):
            if arr[y][x] > i:
                land[y][x] = True

    cnt = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and land[y][x]:
                bfs(y, x)
                cnt += 1
    lands = max(lands, cnt)

    if cnt == 0:
        break

print(lands)