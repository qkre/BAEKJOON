from collections import deque
from sys import stdin

input = stdin.readline


N = int(input())
Q = deque()
for _ in range(N):
    commands = list(input().split())

    if commands[0] == 'push':
        Q.append(commands[1])

    if commands[0] == 'pop':
        if len(Q) != 0:
            print(Q.popleft())
        else:
            print(-1)

    if commands[0] == 'size':
        print(len(Q))

    if commands[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)

    if commands[0] == 'front':
        if len(Q) != 0:
            print(Q[0])
        else:
            print(-1)

    if commands[0] == 'back':
        if len(Q) != 0:
            print(Q[-1])
        else:
            print(-1)