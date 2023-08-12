import math

N, K = map(int, input().split())

primeArr = []

for i in range(1, int(N ** (1 / 2)) + 1):
    if N % i == 0:
        primeArr.append(i)
        if (i**2) != N:
            primeArr.append(N // i)

primeArr.sort()
print(primeArr)
try:
    print(primeArr[K - 1])
except:
    print(0)
