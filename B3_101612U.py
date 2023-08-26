# 전자레인지

T = int(input())
A = 0
B = 0
C = 0

A = T // 300
T -= A * 300
B = T // 60
T -= B * 60
C = T // 10

if T % 10 != 0:
    print(-1)
else:
    print(A, B, C)
