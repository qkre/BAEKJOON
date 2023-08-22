# 구간 합 구하기5
# 누적합, 다이나믹 프로그래밍
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = list(list(map(int, input().split())) for _ in range(N))

positions = list(list(map(int, input().split()) for _ in range(M)))

prefix_board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for row in range(N):
    for col in range(N):
        prefix_board[row + 1][col + 1] = board[row][col]

for row in range(1, N + 1):
    for col in range(1, N + 1):
        prefix_board[row][col] = (
            prefix_board[row][col]
            - prefix_board[row - 1][col - 1]
            + prefix_board[row - 1][col]
            + prefix_board[row][col - 1]
        )

for x1, y1, x2, y2 in positions:
    res = prefix_board[x2][y2]
    res -= prefix_board[x2][y1 - 1]
    res -= prefix_board[x1 - 1][y2]
    res += prefix_board[x1 - 1][y1 - 1]

    print(res)
