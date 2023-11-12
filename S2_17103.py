T = int(input())

sieve = [True] * 1000000

M = int(1000000 ** 0.5)

for i in range(2, M):
    if sieve[i]:
        for j in range(i + i, 1000000, i):
            sieve[j] = False


for case in range(T):
    N = int(input())

    primes = sieve[:N]

    cnt = 0

    for i in range(2, N//2+1):
        if not primes[i]:
            continue

        if not primes[N-i]:
            continue

        cnt += 1

    print(cnt)