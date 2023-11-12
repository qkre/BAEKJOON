N = int(input())

arr = list(int(input()) for _ in range(N))

distances = []

for i in range(N - 1):
    distances.append(arr[i + 1] - arr[i])

distances.sort()

distance_divider = []

for i in range(1, int(distances[0] ** 0.5) + 1):
    if distances[0] % i == 0:
        distance_divider.append(i)
        distance_divider.append(int(distances[0] // i))
distance_divider = list(set(distance_divider))
distance_divider.sort()

GCF = 1

for i in distance_divider:
    P = True
    for j in distances:
        if j % i != 0:
            P = False
            break
    if P:
        GCF = i

cnt = 0
for i in range(arr[0], arr[-1], GCF):
    if i not in arr:
        cnt += 1

print(cnt)
