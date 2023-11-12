from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
weights = []
values = []

for _ in range(N):
    W, V = map(int, input().split())

    weights.append(W)
    values.append(V)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N + 1):
    for weight in range(K+1):
        if i == 0 or weight == 0:
            dp[i][weight] = 0

        elif weights[i-1] <= weight:
            take = values[i-1] + dp[i-1][weight - weights[i-1]]
            dp[i][weight] = max(values[i-1] + dp[i-1][weight - weights[i-1]], dp[i-1][weight])
        else:
            dp[i][weight] = dp[i-1][weight]

print(dp[N][K])