T = int(input())

for case in range(T):
    N = int(input())

    for i in range(N, 4 * (10 ** 10)):
        if i <= 1:
            continue
        is_prime = True
        mid = int(i ** 0.5)

        for j in range(2, mid + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            print(i)
            break
