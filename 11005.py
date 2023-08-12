N, B = map(int, input().split())

nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = []

while N >= B:
    m = int(N % B)
    N = N // B
    result.append(nums[m])

result.append(nums[N])

result.reverse()

print("".join(s for s in result))
