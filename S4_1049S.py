# 기타줄

N, M = map(int, input().split())
guitars = list(list(map(int, input().split())) for _ in range(M))
sum = 0

guitars.sort(key=lambda x: x[0])
each_cost = [y for x, y in guitars]
each_cost.sort()
each_sum = [y * 6 for x, y in guitars]
each_sum.sort()


only_package = (N // 6) * guitars[0][0] if N % 6 == 0 else (N // 6 + 1) * guitars[0][0]
package_each = (N // 6) * guitars[0][0] + (N % 6) * each_cost[0]
only_each = N * each_cost[0]

sum = min(only_package, package_each, only_each)


print(sum)
