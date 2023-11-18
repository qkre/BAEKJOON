from sys import stdin
import itertools

input = stdin.readline

N, M = map(int, input().split())
lines = list(range(1, N + 1))

for _ in range(M):
    A, B = map(int, input().split())
    if lines.index(A) > lines.index(B):
        tmp = lines.index(A)
        lines[lines.index(B)] = A
        lines[tmp] = B

print(*lines)
