# 숨박꼭질
# 그래프, 너비 우선 탐색

N, K = map(int, input().split())

graph = [[N]]
index = 1
while True:
    graph.append([])
    graph[index].append(graph[index - 1][0] + 1)
    graph[index].append(graph[index - 1][0] - 1)
    graph[index].append(graph[index - 1][0] * 2)

    index += 1
