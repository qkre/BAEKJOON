N, M = map(int, input().split())

basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    if i == j:
        basket[i - 1] = k
    for index in range(i - 1, j):
        basket[index] = k

print(*basket)
