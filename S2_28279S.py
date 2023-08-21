from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
deq = deque()

for _ in range(N):
    commands = list(map(int, input().split()))

    if len(commands) == 2:
        if commands[0] == 1:
            deq.appendleft(commands[1])
        else:
            deq.append(commands[1])
    else:
        if commands[0] == 3:
            print(deq.popleft() if deq else -1)
        elif commands[0] == 4:
            print(deq.pop() if deq else -1)
        elif commands[0] == 5:
            print(len(deq))
        elif commands[0] == 6:
            print(0 if deq else 1)
        elif commands[0] == 7:
            print(deq[0] if deq else -1)
        elif commands[0] == 8:
            print(deq[-1] if deq else -1)
