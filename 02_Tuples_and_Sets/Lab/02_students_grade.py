n = int(input())

student_record = {}

for i in range(n):
    data = tuple(input().split())
    student_name, student_grade = data

    if student_name not in student_record:
        student_record[student_name] = []
    student_record[student_name].append(student_grade)


for student_name, student_grades in student_record.items():
    average = sum(list(map(float, student_grades))) / len(student_grades)
    print(f"{student_name} -> {' '.join(student_grades)} (avg: {average:.2f})")