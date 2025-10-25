def add_student(students: dict, name:str):
    if name not in students:
        students[name] = []

def print_student(students: dict, name:str):
    if name in students:
        print(f"{name}:")
        courses = students[name]
        if not courses:
            print(" no completed courses")
        else:
            print(f" {len(courses)} completed courses:")

            for course_name, course_grade in courses:
                print(f"  {course_name} {course_grade}")

            grades = [course_grade for _, course_grade in courses if course_grade > 0]
            avg = mean(grades)
            print(f" average grade {avg}")
    else:
        print(f"{name}: no such person in the database")
    
def mean(grades:list):
    if not grades:
        return 0.0
    total = sum(grades)
    return total / len(grades)

def add_course(students: dict, name:str, course:tuple):
    if name in students:
        courses = students[name]
        course_name = course[0]
        course_grade = course[1]
        updated = False

        for i in range(len(courses)):
            if courses[i][0] == course_name:
                if course_grade > 0 and course_grade > courses[i][1]:
                    students[name][i] = (course_name, course_grade)
                    updated = True
                return
            
        if not updated and course_grade > 0:
            students[name].append(course)

def summary(students: dict):
    most = 0
    most_name = ""
    highest = 0
    highest_name = ""

    print(f"students {len(students)}")

    for name, courses in students.items():
        amount = len(courses)
        if amount > most:
            most_name = name
            most = amount

        grades = [course_grade for _, course_grade in courses if course_grade > 0]
        avg = mean(grades)
        if avg > highest:
            highest_name = name
            highest = avg

    print(f"most courses completed {most} {most_name}")
    print(f"best average grade {highest} {highest_name}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)