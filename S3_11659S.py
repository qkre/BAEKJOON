import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = []
for i in range(N):
    if i == 0:
        prefix_sum.append(nums[i])
    else:
        prefix_sum.append(prefix_sum[i - 1] + nums[i])

course = []
for _ in range(M):
    i, j = map(int, input().split())
    if i == j:
        if i != 1:
            print(prefix_sum[j - 1] - prefix_sum[i - 2])
        else:
            print(prefix_sum[i - 1])

    elif i != 1:
        print(prefix_sum[j - 1] - prefix_sum[i - 2])

    else:
        print(prefix_sum[j - 1])
