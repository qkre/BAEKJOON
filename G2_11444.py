N = int(input())


C = 1000000007

A, B = 0, 1

for i in range(N):
    temp = B % C
    B = A % C + B % C
    A = temp

print(A)

