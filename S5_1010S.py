# 다리 놓기
# 수학, 다이나믹 프로그래밍, 조합론
import math

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    bridge = math.factorial(M) // (math.factorial(M - N) * math.factorial(N))
    print(bridge)
