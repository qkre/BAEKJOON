from sys import stdin

input = stdin.readline

N = int(input())

tree = [[] for _ in range(N)]

for _ in range(N - 1):
    S, E = map(int, input().split())

    tree[S - 1].append(E)

seq = list(map(int, input().split()))

check = [False] * N
ans = []
visited = []


def dfs(x):
    visited.append(x)
    if check[x - 1]:
        return
    for i in tree[x - 1]:
        if not check[i - 1]:
            check[x - 1] = True
            dfs(i)
            check[x - 1] = False



dfs(1)
ans.append(visited)
visited = []
