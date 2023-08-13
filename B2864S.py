A, B = map(list, input().split())

for i in range(len(A)):
    if A[i] == "6":
        A[i] = "5"

for i in range(len(B)):
    if B[i] == "6":
        B[i] = "5"


min = int("".join(A)) + int("".join(B))


for i in range(len(A)):
    if A[i] == "5":
        A[i] = "6"

for i in range(len(B)):
    if B[i] == "5":
        B[i] = "6"

max = int("".join(A)) + int("".join(B))

print(min, max)
