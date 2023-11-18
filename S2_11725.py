from sys import stdin
import sys

sys.setrecursionlimit(10**5)

input = stdin.readline

N = int(input())

tree = list([] for _ in range(N + 1))
root = dict()
for _ in range(N - 1):
    S, E = map(int, input().split())

    tree[S].append(E)
    tree[E].append(S)


def dfs(s):

    for i in tree[s]:
        if not visited[i]:
            root[i] = s
            visited[i] = True
            dfs(i)

visited = [False] *(N + 1)
dfs(1)

for i in range(2, N+1):
    print(root[i])