N = int(input())

tree = ["" for _ in range(N)]

for i in range(1, N+1):
    node, left, right = input().split()
    tree[i-1] = node
    tree[i * 2 - 1] = left
    tree[i * 2] = right
