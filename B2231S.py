N = int(input())


for i in range(N):
    i_string = list(str(i))
    if N == i + sum(map(int, i_string)):
        print(i)
        quit()
print(0)
