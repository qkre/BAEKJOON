import sys

sys.setrecursionlimit(10**5)

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))

dp = [0] * (N + 1)

def dfs(s, e, depth, values):
    global N

    if depth == e:
        dp[e] = max(dp[e], values)
        return

    for i in range(s, N):
        if i + arr[i][0] <= N:
            dfs(i + arr[i][0], e, depth+1, values + arr[i][1])


for i in range(1, N+1):

    for j in range(N):
        if j + arr[j][0] <= N:
            dfs(j + arr[j][0], i, 1, arr[j][1])

print(max(dp))