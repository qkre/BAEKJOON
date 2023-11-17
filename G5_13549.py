N, K = map(int, input().split())


def bfs(s, e):
    q = [s]
    visited = [0] * 200001
    checked = [False] * 200001

    while q:
        n = q.pop(0)

        if n == e:
            break

        if 0 <= n * 2 <= 200000 and not checked[n * 2]:
            visited[n * 2] = visited[n]
            checked[n * 2] = True
            q.append(n * 2)

        if 0 <= n - 1 <= 200000 and not checked[n - 1]:
            visited[n - 1] = visited[n] + 1
            checked[n - 1] = True
            q.append(n - 1)

        if 0 <= n + 1 <= 200000 and not checked[n + 1]:
            visited[n + 1] = visited[n] + 1
            checked[n + 1] = True
            q.append(n + 1)

    return visited[e]


ans = bfs(N, K)

print(ans)
