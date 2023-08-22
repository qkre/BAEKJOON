# 알파벳
# 그래프, 깊이 우선 탐색, 백트랙킹
import sys

input = sys.stdin.readline

global R, C
R, C = map(int, input().split())
board = list(list(input().split()[0]) for _ in range(R))
visited_path = [[False for _ in range(C)] for _ in range(R)]
visited_alpahbet = [False for _ in range(26)]

global max
max = 1


def dfs(X, Y, board, visited_path, visited_alphabet, cnt):
    global max, R, C
    if cnt > max:
        max = cnt

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    for i in range(4):
        nx = X + dx[i]
        ny = Y + dy[i]

        if nx < 0 or ny < 0 or nx >= C or ny >= R:
            continue
        elif not visited_path[ny][nx] and not visited_alpahbet[ord(board[ny][nx]) - 65]:
            visited_path[ny][nx] = True
            visited_alpahbet[ord(board[ny][nx]) - 65] = True
            dfs(nx, ny, board, visited_path, visited_alphabet, cnt + 1)
            visited_path[ny][nx] = False
            visited_alpahbet[ord(board[ny][nx]) - 65] = False


visited_path[0][0] = True
visited_alpahbet[ord(board[0][0]) - 65] = True
dfs(0, 0, board, visited_path, visited_alpahbet, 1)

print(max)
