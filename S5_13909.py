N = int(input())

cnt = 1

index = 2

if index < 2:
    print(1)
    quit()

while True:
    if index ** 2 > N:
        break
    else:
        cnt += 1
        index += 1


print(cnt)