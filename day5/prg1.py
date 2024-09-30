students_height = input("Enter the height of all the students").split()
for n in range(0,len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)
sum=0
count=0
for i in students_height:
    sum += i
    count +=1

result =round(sum/count)
print(f"Avg is: {result}")