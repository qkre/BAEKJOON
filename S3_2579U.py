import sys

input = sys.stdin.readline

N = int(input())

arr = list(int(input()) for _ in range(N))

dp = [[0, 0, 0] for _ in range(N+1)]

for i in range(1, N+1):

    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + arr[i-1]
    dp[i][2] = dp[i-1][1] + arr[i-1]

print(max(dp[-1][1], dp[-1][2]))