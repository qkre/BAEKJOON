from sys import stdin
import heapq

input = stdin.readline

N = int(input())

heap = []
ans = [0]
for _ in range(N):
    heapq.heappush(heap, int(input()))

while len(heap) > 1:
    A = heapq.heappop(heap)
    B = heapq.heappop(heap)

    heapq.heappush(heap, A + B)
    ans.append(A + B)

print(sum(ans))
