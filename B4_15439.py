N = int(input())

fac = [1, 1]

for i in range(2, N+1):
    fac.append(i * fac[i-1])

if N == 1:
    print(0)
    quit()

print(fac[N] // fac[N-2])