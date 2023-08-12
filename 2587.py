import math

nums = []
for _ in range(5):
    nums.append(int(input()))

print(int(sum(nums) / 5))
nums.sort()
print(nums[2])
