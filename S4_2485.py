N = int(input())

arr = list(int(input()) for _ in range(N))

distances = []

for i in range(N - 1):
    distances.append(arr[i + 1] - arr[i])

distances = list(set(distances))

distances.sort()

if len(distances) == 1:
    print(0)
    quit()

GCF = 1

divisor = []

for i in range(1, int(distances[0] ** 0.5) + 1):
    if distances[0] % i == 0:
        divisor.append(i)
        divisor.append(distances[0] // i)

for i in divisor:
    passed = True
    for j in distances:
        if j % i != 0:
            passed = False
            break
    if passed:
        GCF = max(GCF, i)

cnt = ((arr[-1] - arr[0]) // GCF) - len(arr) + 1

print(cnt)
