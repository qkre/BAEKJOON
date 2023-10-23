global A, B

A, B = map(int, input().split())


def GCD(a, b):
    global A, B
    if a % b == 0:
        print(A * B // b)
    else:
        GCD(b, a % b)


GCD(A, B)
