N, K = map(int, input().split())

C = 1000000007

def power(N, P):
    global C

    if P == 0:
        return 1

    half = power(N, P // 2)

    if P % 2 == 0:
        return ((half % C) ** 2) % C
    else:
        return ((half * N) % C) * (half % C) % C

fac = [1] * 4000001

for i in range(1, 4000001):
    fac[i] = (fac[i-1] * i) % C

top = fac[N] % C
bottom = (fac[N-K] % C) * (fac[K] % C)
bottom_reversed = power(bottom, C - 2)

ans = top * bottom_reversed % C

print(ans)