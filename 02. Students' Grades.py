number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    student_info = input().split(' ')
    name = student_info[0]
    grade = float(student_info[1])
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for student, grades in students.items():
    average_grade = 0
    result = f'{student} -> '

    for grade in grades:
        result += f'{grade:.2f} '
        average_grade += grade

    average_grade /= len(grades)

    result += f'(avg: {average_grade:.2f})'
    print(result)