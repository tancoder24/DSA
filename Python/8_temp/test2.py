# result
result = []

# students
students = []

# C is no of clg
# N is no of student 
C, N = list(map(int, input().split()))

# clg seats index 0 is clg1
C_seats = list(map(int, input().split()))

for i in range(N):
    stud = input().split(",")
    student = {
        "name": stud[0],
        "percentage": float(stud[1]),
        "choice1": stud[2],
        "choice2": stud[3],
        "choice3": stud[4],
    }
    students.append(student)

students = sorted(students, key=lambda d: int(d['name'].split("-")[-1]))
students = sorted(students, key=lambda d: d['percentage'], reverse=True)
print(students)

for student in students:
    if C_seats[int(student["choice1"].split("-")[-1]) - 1] > 0:
        C_seats[int(student["choice1"][-1]) - 1]  -= 1
        name = student["name"]
        clg = student["choice1"]
        result.append(f"{name} {clg}")

    elif C_seats[int(student["choice2"][-1]) - 1] > 0:
        C_seats[int(student["choice2"][-1]) - 1]  -= 1
        name = student["name"]
        clg = student["choice2"]
        result.append(f"{name} {clg}")

    elif C_seats[int(student["choice3"][-1]) - 1] > 0:
        C_seats[int(student["choice3"][-1]) - 1]  -= 1
        name = student["name"]
        clg = student["choice3"]
        result.append(f"{name} {clg}")

for res in result:
    print(res)