# 그리디 알고리즘

while True:
    try:
        A, B, C = map(int, input().split())

        print(max((C - B - 1), (B - A - 1)))

    except EOFError:
        quit()
