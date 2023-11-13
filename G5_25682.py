N, M, K = map(int, input().split())

chess_board = list(list(input()) for _ in range(N))


def count_block(state, y, x, ey, ex):
    if state == 0:
        cnt = 0
        for i in range(y, ey):
            for j in range(x, ex):
                if i % 2 == 0 and j % 2 == 0:
                    if chess_board[i][j] != 'B':
                        cnt += 1
                elif i % 2 != 0 and j % 2 != 0:
                    if chess_board[i][j] != 'B':
                        cnt += 1
                else:
                    if chess_board[i][j] != 'W':
                        cnt += 1

    else:
        cnt = 0
        for i in range(y, ey):
            for j in range(x, ex):
                if i % 2 == 0 and j % 2 == 0:
                    if chess_board[i][j] != 'W':
                        cnt += 1
                elif i % 2 != 0 and j % 2 != 0:
                    if chess_board[i][j] != 'W':
                        cnt += 1
                else:
                    if chess_board[i][j] != 'B':
                        cnt += 1

    return cnt


cnt = K * K

for y in range(N - K + 1):
    for x in range(M - K + 1):
        cnt = min(cnt, count_block(0, y, x, y + K, x + K))
        cnt = min(cnt, count_block(1, y, x, y + K, x + K))

print(cnt)
