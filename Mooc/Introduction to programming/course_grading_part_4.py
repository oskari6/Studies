# write your solution here
def read_files(students_info, exercises_info, exam_point_info, course_info):
    students = {}
    exercise_points = {}
    exercise_sum = {}
    exam_points = {}
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
            exercise_points[parts[0]] = sum // 4
            exercise_sum[parts[0]] = sum

    with open(exam_point_info) as file:
            for line in file:
                sum = 0
                parts = line.strip().split(';')
                if parts[0] == "id":
                    continue
                for num in parts[1:]:
                    sum += int(num)
                exam_points[parts[0]] = sum
    
    with open(course_info) as file:
        for line in file:
            line = line.strip()
            if line.startswith("name"):
                course = line.split(":")[1].strip()
            if line.startswith("study"):
                credits = int(line.split(":")[1].strip())

    with open("results.txt", "w") as file:
        file.write(f"{course}, {credits} credits\n")
        file.write("======================================\n")
        file.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n")

        for id, name in students.items():
            total = 0
            grade = 0
            if id in exam_points:
                total += exam_points[id]
            if id in exercise_points:
                total += exercise_points[id]
            if total >= 0 and total <= 14:
                grade = 0
            elif total >= 15 and total <= 17:
                grade = 1
            elif total >= 18 and total <= 20:
                grade = 2
            elif total >= 21 and total <= 23:
                grade = 3
            elif total >= 24 and total <= 27:
                grade = 4
            elif total >= 28:
                grade = 5

            file.write(f"{name:30}{exercise_sum.get(id, 0):<10}{exercise_points.get(id, 0):<10}{exam_points.get(id, 0):<10}{total:<10}{grade:<10}\n")

        with open("results.csv", "w") as file:
            for id, name in students.items():
                total = 0
                grade = 0
                if id in exam_points:
                    total += exam_points[id]
                if id in exercise_points:
                    total += exercise_points[id]
                if total >= 0 and total <= 14:
                    grade = 0
                elif total >= 15 and total <= 17:
                    grade = 1
                elif total >= 18 and total <= 20:
                    grade = 2
                elif total >= 21 and total <= 23:
                    grade = 3
                elif total >= 24 and total <= 27:
                    grade = 4
                elif total >= 28:
                    grade = 5

                file.write(f"{id};{name};{grade}\n")

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_point_info = input("Exam Points: ")
    course_info = input("Course information:")
    read_files(student_info, exercise_data, exam_point_info, course_info)
else:
    # hard-coded input
    student_info = "students2.csv"
    exercise_data = "exercises2.csv"
    exam_point_info = "exam_points2.csv"
    course_info = "course1.txt"
    read_files(student_info, exercise_data, exam_point_info, course_info)