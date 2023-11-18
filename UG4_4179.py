from collections import deque

R, C = map(int, input().split())

arr = list(list(input()) for _ in range(R))
visited = list([False] * C for _ in range(R))
fire_q = deque()

for y in range(R):
    for x in range(C):
        if arr[y][x] == "J":
            J = (y, x)
        if arr[y][x] == 'F':
            fire_q.append((y, x))


def move_fire(q):
    global R, C
    new_fire_q = deque()

    while q:
        y, x = q.popleft()

        dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < R and 0 <= nx < C and arr[ny][nx] == '.':
                new_fire_q.append((ny, nx))
                arr[ny][nx] = 'F'

    return new_fire_q


def bfs(J):
    global R, C, fire_q

    q = deque()
    q.append(J)
    while q:
        y, x = q.popleft()
        visited[y][x] = True

        if y == 0 or y == R - 1 or x == 0 or x == C - 1:
            if arr[y][x] == 'J':
                return 1

            return arr[y][x] + 1

        dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < R and 0 <= nx < C and arr[ny][nx] == '.' and not visited[ny][nx]:
                if arr[y][x] == '.' or arr[y][x] =='J':
                    arr[y][x] = '.'
                    arr[ny][nx] = 1
                else:
                    arr[ny][nx] = arr[y][x] + 1
                    arr[y][x] = '.'

                q.append((ny, nx))


        print("==========================")
        for _ in arr:
            print(''.join(list(map(str, _))))
        print("==========================")

        fire_q = move_fire(fire_q)
    return "IMPOSSIBLE"


print(bfs(J))
