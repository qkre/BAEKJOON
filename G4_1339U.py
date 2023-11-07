import copy
from collections import deque

N = int(input())

word_list = list(deque(input()) for _ in range(N))
word_list.sort(key=lambda x: len(x), reverse=True)

num_dict = {}
num = 9


