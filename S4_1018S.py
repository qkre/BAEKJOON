# 체스판 다시 칠하기
# 브루트포스 알고리즘
from sys import stdin
import copy

input = stdin.readline

global N, M

N, M = map(int, input().split())

board = list(list(input().split()[0]) for _ in range(N))
global min_cnt
min_cnt = 9999999999999999


def check(sx, sy, x, y, board, visited, cnt, depth):
    global min_cnt, N, M

    if depth == 64:
        min_cnt = min(cnt, min_cnt)
        return

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < sx or ny < sy or nx >= M or ny >= N or nx >= sx + 8 or ny >= sy + 8:
            continue
        elif board[y][x] != board[ny][nx] and not visited[ny][nx]:
            visited[ny][nx] = True
            check(sx, sy, nx, ny, board, visited, cnt, depth + 1)
        elif board[y][x] == board[ny][nx] and not visited[ny][nx]:
            visited[ny][nx] = True
            if board[y][x] == "B":
                board[ny][nx] = "W"
            else:
                board[ny][nx] = "B"
            check(sx, sy, nx, ny, board, visited, cnt + 1, depth + 1)


for y in range(N - 7):
    for x in range(M - 7):
        new_board = copy.deepcopy(board)
        visited = list(list([False for _ in range(M)]) for _ in range(N))
        visited[y][x] = True
        check(x, y, x, y, new_board, visited, 0, 1)
        new_board = copy.deepcopy(board)
        new_board[y][x] = "B" if new_board[y][x] == "W" else "W"
        visited = list(list([False for _ in range(M)]) for _ in range(N))
        visited[y][x] = True
        check(x, y, x, y, new_board, visited, 1, 1)


print(min_cnt)
