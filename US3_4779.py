def left(N, s):
    if N == 1:
        return

    start = s + N // 3
    end = s + (N // 3 * 2)

    S[start: end] = [" "] * (N // 3)
    print(''.join(S))

    left(N // 3, s)
    right(N // 3, end)


def right(N, s):
    if N == 1:
        return

    start = s + N // 3
    end = s + (N // 3 * 2)

    S[start: end] = [" "] * (N // 3)
    print(''.join(S))

    left(N // 3, end)
    right(N // 3, end)


while True:
    try:
        N = int(input())
        S = list("-" * 3 ** N)

        left(3 ** N, 0)
        right(3 ** N, 0)

        print(''.join(S))
    except:
        break
