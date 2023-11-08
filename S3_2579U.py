import sys

input = sys.stdin.readline

N = int(input())

arr = list(int(input()) for _ in range(N))

dp = [0] * N

for i in range(N-1):
    dp[i] =max(dp[i-1] + arr[i], dp[i-1] + arr[i+1])
     
