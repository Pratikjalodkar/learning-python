students_scores = input("Enter the height of all the students").split()
for n in range(0,len(students_scores)):
    students_scores[n] = int(students_scores[n])
print(students_scores)
max=students_scores[0]
for i in students_scores:
    if(i<max):
        continue
    else:
        max=i
print(max)