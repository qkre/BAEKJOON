# 알파벳
# 그래프, 깊이 우선 탐색, 백트랙킹

R, C = map(int, input().split())

path_check = list([False for _ in range(C)] for _ in range(R))

path_alpah_list = []

board = list(list(input()) for _ in range(R))


max_move = 0
