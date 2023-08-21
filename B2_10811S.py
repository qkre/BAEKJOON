import sys

input = sys.stdin.readline

N, M = map(int, input().split())
basket = [i for i in range(1, N + 1)]
for _ in range(M):
    S, E = map(int, input().split())
    S -= 1
    basket[S:E] = list(reversed(basket[S:E]))

print(*basket)
