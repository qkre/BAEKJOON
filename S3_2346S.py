from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().split()))
checked = [False for _ in range(N)]
ans = []
index = 0
cnt = 0
while cnt != N:
    cnt += 1
    checked[index] = True
    n = balloons[index]
    ans.append(index + 1)
    if len(ans) == N:
        print(*ans)
        quit()
    for i in range(n):
        index += 1
        if index >= N:
            index = 0
        while checked[index]:
            index += 1
            if index >= N:
                index = 0
    for i in range(0, n, -1):
        index -= 1
        if index < 0:
            index = N - 1
        while checked[index]:
            index -= 1
            if index < 0:
                index = N - 1

print(cnt)
