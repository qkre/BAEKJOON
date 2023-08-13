T = int(input())

MEMORY = [[] for _ in range(100)]

for _ in range(T):
    count = 0
    n, m = map(int, input().split())
    if not MEMORY[m]:
        for a in range(1, n):
            for b in range(a + 1, n):
                if (a**2 + b**2 + m) % (a * b) == 0:
                    MEMORY[m].append([a, b])
    else:
        for a in range(MEMORY[m][-1][0], n):
            for b in range(a + 1, n):
                if (a**2 + b**2 + m) % (a * b) == 0:
                    MEMORY[m].append([a, b])

    print(MEMORY[m])
    print(len(MEMORY[m]))
