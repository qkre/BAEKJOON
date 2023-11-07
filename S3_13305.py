N = int(input())
weight = list(map(int, input().split()))
visited = [False] * N
cost = list(map(int, input().split()))

ans = 0
index = 0
while True:
    cnt = 1
    if index >= N:
        break
    for i in range(1, N - index):
        if cost[index] < cost[index + i]:
            cnt += 1
        else:
            break
    tmp = weight[index : index + cnt]
    ans += sum(tmp) * cost[index]
    index += cnt

print(ans)
