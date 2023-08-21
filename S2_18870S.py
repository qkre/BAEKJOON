N = int(input())
nums = list(map(int, input().split()))
sorted = sorted(list(set(nums)))
indexOf = {}
for i in range(len(sorted)):
    indexOf[sorted[i]] = i
result = []
for num in nums:
    result.append(indexOf[num])

print(*result)
