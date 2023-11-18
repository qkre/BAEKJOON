from sys import stdin
import heapq

input = stdin.readline

N = int(input())
M = int(input())

q = list([] for _ in range(N + 1))

dp = [100001 * N] * (N + 1)

for _ in range(M):
    S, E, C = map(int, input().split())

    heapq.heappush(q[S], (C, E))


def dijkstra(start):
    dp[start] = 0

    priority_q = []
    heapq.heappush(priority_q, (0, start))

    while priority_q:
        current = priority_q[0][1]

        weight = priority_q[0][0]

        heapq.heappop(priority_q)

        if dp[current] < weight:
            continue

        for i in range(len(q[current])):
            next = q[current][i][1]
            next_weight = weight + q[current][i][0]

            if next_weight < dp[next]:
                dp[next] = next_weight
                heapq.heappush(priority_q, (next_weight, next))


S, E = map(int, input().split())

dijkstra(S)

print(dp[E])
