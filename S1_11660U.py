import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
prefix_board = []
for y in range(N):
    numbers = list(map(int, input().split()))
    board.append(numbers)
    prefix_board.append([])
    for x in range(N):
        if x == 0:
            prefix_board[y].append(board[y][x])
        else:
            prefix_board[y].append(board[y][x] + prefix_board[y][x - 1])

positions = [list(map(int, input().split())) for _ in range(M)]

for y1, x1, y2, x2 in positions:
    res = 0
    for i in range(y2 - y1 + 1):
        Y = y1 - 1 + i if y1 - 1 + i >= 0 else 0
        X2 = x2 - 1
        X1 = x1 - 2
        if X1 < 0:
            res += prefix_board[Y][X2]
        else:
            res += prefix_board[Y][X2] - prefix_board[Y][X1]
    print(res)
