from collections import deque

N, K = map(int, input().split())


def bfs(start, end):
    q = [start]
    checked = [0] * 200001
    checked[start] = 1

    while q:
        c = q.pop(0)

        if c == end:
            return checked[end] - 1

        for n in (c-1, c+1, c*2):
            if 0 <= n <= 200000 and checked[n] == 0:
                q.append(n)
                checked[n] = checked[c] + 1



ans = bfs(N, K)

print(ans)