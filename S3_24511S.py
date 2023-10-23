from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue = deque()
ans = deque()
for i in range(N):
    if A[i] == 0:
        queue.append(B[i])

for i in C:
    queue.appendleft(i)
    print(queue.pop(), end=" ")
