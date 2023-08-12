N = int(input())
words = []
for _ in range(N):
    words.append(input())

qm_index = words.index("?")

M = int(input())
cand = []
for _ in range(M):
    cand.append(input())

if N == 1:
    print(cand[0])
    quit()

if qm_index == 0:
    alpah = words[1][0]
    for word in cand:
        if word[-1] == alpah and word not in words:
            print(word)
            quit()
elif qm_index == N - 1:
    alpah = words[-2][-1]
    for word in cand:
        if word[0] == alpah and word not in words:
            print(word)
            quit()
else:
    before_alpah = words[qm_index - 1][-1]
    next_alpah = words[qm_index + 1][0]
    for word in cand:
        if word[0] == before_alpah and word[-1] == next_alpah and word not in words:
            print(word)
            quit()
