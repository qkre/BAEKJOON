# 그리디 알고리즘

N = int(input())

stores = list(map(int, input().split()))

count = 0
next_milk = 0

for milk in stores:
    if milk == next_milk:
        count += 1
        next_milk += 1
        if next_milk == 3:
            next_milk = 0

print(count)
