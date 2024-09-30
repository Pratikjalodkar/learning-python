# Grading Program

student_score = {
    "A":81,
    "B":70,
    "C":65,
    "D":88,
    "E":45,
    "F":58
    }

for student in student_score:
    score=student_score[student]
    if score>90:
        student_score[student] = "Outstanding.."
    elif score>80:
        student_score[student] = "Exceeding Expectation.."
    elif score>70:
        student_score[student] = "Acceptable.."
    else:
        student_score[student] = "Fail.."

print(student_score)