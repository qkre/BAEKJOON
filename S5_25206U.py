# 너의 평점은
# 수학, 구현, 문자열
from sys import stdin

input = stdin.readline
score_count = [[] for _ in range(4)]
for _ in range(20):
    title, credit, score = input().split()
    credit = int(float(credit))
    score_count[credit - 1].append(score)
avg_score = 0
whole_credit = 0
for i in range(1, 5):
    scores = score_count[i - 1]
    if len(scores) > 0:
        AP = scores.count("A+")
        A = scores.count("A0")
        BP = scores.count("B+")
        B = scores.count("B0")
        CP = scores.count("C+")
        C = scores.count("C0")
        DP = scores.count("D+")
        D = scores.count("D0")
        F = scores.count("F")
        P = scores.count("P")
        avg_score += (
            (4.5 * AP)
            + (4.0 * A)
            + (3.5 * BP)
            + (3.0 * B)
            + (2.5 * CP)
            + (2.0 * C)
            + (1.5 * DP)
            + (1.0 * D)
        )
        whole_credit += (len(scores) - P) * i

print(avg_score / whole_credit)
