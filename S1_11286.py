from sys import stdin
import heapq

input = stdin.readline

N = int(input())

heap = []
for _ in range(N):
    cmd = int(input())

    if cmd == 0:
        if len(heap) > 0:
            s = heapq.heappop(heap)
            print(s[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(cmd), cmd))
