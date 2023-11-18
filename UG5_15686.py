from sys import stdin
import itertools

input = stdin.readline

N, M = map(int, input().split())

combi = list(itertools.combinations(range(M), M))

city = list(list(map(int, input().split())) for _ in range(N))

house_pos = list()
shop_pos = list()
survived = list()

for row in range(N):
    for col in range(N):
        if city[row][col] == 1:
            house_pos.append([row, col])
        elif city[row][col] == 2:
            shop_pos.append([row, col])
