socks = [int(input()) for _ in range(5)]
for i in socks:
    if socks.count(i) % 2 != 0:
        print(i)
        quit()
