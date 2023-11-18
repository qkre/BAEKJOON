from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))
visited = list([False] * M for _ in range(N))
ans = list([0] * M for _ in range(N))


def bfs():
    global N, M
    q = deque()

    for y in range(N):
        for x in range(M):
            if arr[y][x] == 2:
                q.append((y, x))
                break
        if q:
            break

    while q:
        y, x = q.popleft()
        visited[y][x] = True
        dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and arr[ny][nx] != 0:
                ans[ny][nx] = ans[y][x] + 1
                visited[ny][nx] = True
                q.append((ny, nx))


bfs()

for y in range(N):
    for x in range(M):
        if arr[y][x] != 0 and not visited[y][x]:
            ans[y][x] = -1

for _ in ans:
    print(*_)
