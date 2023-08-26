# 누울 자리를 찾아라

from sys import stdin

input = stdin.readline

N = int(input())
room = list(list(input().rstrip()) for _ in range(N))

row = 0
col = 0

for i in range(N):
    check = False
    for j in range(N - 1):
        if room[i][j] == "." and room[i][j + 1] == ".":
            check = True
        else:
            if check:
                col += 1
                check = False
    if check:
        col += 1

for i in range(N):
    check = False
    for j in range(N - 1):
        if room[j][i] == "." and room[j + 1][i] == ".":
            check = True
        else:
            if check:
                row += 1
                check = False
    if check:
        row += 1

print(col, row)
