import heapq

INF = 10 ** 10

V, E = map(int, input().split())

K = int(input())

d = [INF] * (V+1)

q = list([] for _ in range(V+1))

for i in range(1, E+1):
    s, e, w = map(int, input().split())

    heapq.heappush(q[s], (w, e))

def dijkstra(start):
    d[start] = 0

    pq = []

    heapq.heappush(pq, (0, start))

    while len(pq) != 0:
        current = pq[0][1]

        weight = pq[0][0]

        heapq.heappop(pq)

        if d[current] < weight:
            continue

        for i in range(len(q[current])):
            next = q[current][i][1]
            next_weight = weight + q[current][i][0]

            if next_weight < d[next]:
                d[next] = next_weight
                heapq.heappush(pq, (next_weight, next))

dijkstra(K)

d = d[1:]

for i in d:
    if i == INF:
        print("INF")
    else:
        print(i)

# graph = list([INF] * V for _ in range(V))
# visited = [False] * V
# d = [0] * V
# for _ in range(E):
#     s, e, w = map(int, input().split())
#
#     graph[s - 1][e - 1] = w
#     graph[s - 1][s - 1] = 0
#
# def get_small_idx():
#     global  graph, d
#     min_weight = INF
#     index = 0
#
#     for i in range(V):
#         if d[i] < min_weight and not visited[i]:
#             min_weight = d[i]
#             index = i
#
#     return index
#
#
# def dijkstra(start):
#     global graph, d
#     for i in range(V):
#         d[i] = graph[start][i]
#
#     visited[start] = True
#
#     for i in range(V):
#         current = get_small_idx()
#         for j in range(V):
#             if not visited[j]:
#                 if d[current] + graph[current][j] < d[j]:
#                     d[j] = d[current] + graph[current][j]
#
#
# dijkstra(K - 1)
#
# for i in d:
#     if i == INF:
#         print("INF")
#     else:
#         print(i)