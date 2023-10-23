import itertools

length = int(input())

K = ("A" * (length - 2)) + ("B" * (2))

answer = itertools.permutations(K)
cnt = 0
for i in answer:
    cnt += 1
    print(f"{cnt} ::: {i}")
    if cnt == 24:
        break
