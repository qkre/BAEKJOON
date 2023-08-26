# 에어팟

N = int(input())
battery = list(map(int, input().split()))

use = 0
last_use = 2
for i in range(N):
    if i == 0:
        use += 2
    else:
        if battery[i - 1] == battery[i]:
            use += last_use * 2
            last_use *= 2
            if use > 100:
                use = 0
                last_use = 1
        else:
            use += 2
            last_use = 2

print(use)
