from sys import stdin
from collections import deque

input = stdin.readline
N, L = map(int, input().split())
arr = list(map(int, input().split()))
ans = list()

for i in range(N):
    head = i + 1 - L
    tail = i + 1
    if head < 0:
        ans.append(min(arr[:tail]))
    else:
        ans.append(min(arr[head:tail]))

print(*ans)
