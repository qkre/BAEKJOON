# 올림픽

from sys import stdin
from collections import deque

input = stdin.readline

N, K = map(int, input().split())

nations = list(list(map(int, input().split())) for _ in range(N))
score = [0 for _ in range(N)]
rank = deque()

for i in range(N):
    score[i] = nations[i][1] * 3 + nations[i][2] * 2 +nations[i][3]


for i in range(N):
    if len(rank) == 0:
        rank.append(i)
    else:
        if score[rank[0]] < score[i]:
            rank.appendleft(i)
        if score[rank[0]]
