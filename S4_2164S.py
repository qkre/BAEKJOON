from collections import deque

N = int(input())

nums = deque([i for i in range(1, N + 1)])

while len(nums) != 1:
    nums.popleft()
    nums.append(nums.popleft())

print(*nums)
