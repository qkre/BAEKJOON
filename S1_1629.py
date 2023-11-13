A, B, C = map(int, input().split())


def power(N, p):
    global C

    if p == 0:
        return 1

    half = power(N, p // 2)

    if p % 2 == 0:
        return ((half % C) ** 2) % C
    else:
        return (((half * N) % C) * (half % C)) % C


print(power(A, B))
