credit_sum = 0
grade_sum = 0

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade == "A+":
        grade_sum += credit * 4.5
        credit_sum += credit

    elif grade == "A0":
        grade_sum += credit * 4.0
        credit_sum += credit
    elif grade == "B+":
        grade_sum += credit * 3.5
        credit_sum += credit
    elif grade == "B0":
        grade_sum += credit * 3.0
        credit_sum += credit
    elif grade == "C+":
        grade_sum += credit * 2.5
        credit_sum += credit
    elif grade == "C0":
        grade_sum += credit * 2.0
        credit_sum += credit
    elif grade == "D+":
        grade_sum += credit * 1.5
        credit_sum += credit
    elif grade == "D0":
        grade_sum += credit * 1.0
        credit_sum += credit
    elif grade == "F":
        grade_sum += 0
        credit_sum += credit
    else:
        continue

ans = grade_sum / credit_sum

print(f"{ans:.6f}")
