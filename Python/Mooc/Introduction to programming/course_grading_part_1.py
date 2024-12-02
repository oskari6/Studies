# write your solution here
def read_files(students_info, exercises_info):
    students = {}
    exercises = {}
    with open(students_info) as file:
        for line in file:
            parts = line.strip().split(';')
            if parts[0] == "id":
                continue
            students[parts[0]] = parts[1] + " " + parts[2]

    with open(exercises_info) as file:
        for line in file:
            sum = 0
            parts = line.strip().split(';')
            if parts[0] == "id":
                continue
            for num in parts[1:]:
                sum += int(num)
            exercises[parts[0]] = sum

    for id, name in students.items():
        if id in exercises:
            completed = exercises[id]
            print(f"{name} {completed}")


if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    read_files(student_info, exercise_data)
else:
    # hard-coded input
    student_info = "students2.csv"
    exercise_data = "exercises2.csv"
    

