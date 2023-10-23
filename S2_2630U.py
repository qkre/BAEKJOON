from sys import stdin

input = stdin.readline

N = int(input())

global board, visited, blue, white, is_rect


blue, white = 0, 0
board = list(list(map(int, input().split())) for _ in range(N))
visited = list([False for _ in range(N)] for _ in range(N))
is_rect = False


def check(startX, startY, x, y, depth, count, color):
    global board, visited, is_rect, origin

    if depth**2 == count:
        is_rect = True

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y

        if (
            nx < startX
            or ny < startY
            or nx >= x + depth
            or ny >= y + depth
            or nx >= origin
            or ny >= origin
            or visited[ny][nx]
            or board[ny][nx] != color
        ):
            continue

        visited[ny][nx] = True
        print("====================")
        for _ in visited:
            print(_)
        check(startX, startY, nx, ny, depth, count + 1, color)
        if not is_rect:
            visited[ny][nx] = False


origin = N
while N >= 1:
    for y in range(origin):
        for x in range(origin):
            is_rect = False
            if not visited[y][x]:
                visited[y][x] = True
                check(x, y, x, y, N, 1, board[y][x])
                if not is_rect:
                    visited[y][x] = False

    N /= 2


print(blue, white)
