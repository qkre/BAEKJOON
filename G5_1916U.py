# 최소비용 구하기
# 그래프, 데이크스트라
from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
information = list(list(map(int, input().split())) for _ in range(M))
visited = [False for _ in range(N)]
global departure, destination, min_cost

departure, destination = map(int, input().split())

min_cost = 10000000000


def dfs(s, information, visited, cost):
    global departure, destination, min_cost
    if s == destination - 1:
        min_cost = min(min_cost, cost)
        return

    for info in information:
        if info[0] - 1 != s:
            continue
        elif not visited[info[1] - 1]:
            visited[info[1] - 1] = True
            dfs(info[1] - 1, information, visited, cost + info[2])
            visited[info[1] - 1] = False


visited[departure - 1] = True
dfs(departure - 1, information, visited, 0)

print(min_cost)
