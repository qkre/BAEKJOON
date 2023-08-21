N = int(input())
HEIGHT = list(map(int, input().split()))

now = 0
count = 0
while now < N:
    count += 1
    index = 1
    while True:
        try:
            if HEIGHT[now] > HEIGHT[now + index]:
                now += 1
            else:
                now += 1
                break
        except:
            now += 1
            break

print(count)
