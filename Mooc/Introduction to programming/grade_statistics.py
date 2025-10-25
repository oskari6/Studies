def grade_input():
    exams = []
    exercises = []
    while True:
        data = input("Enter exam points and exercises completed (or press Enter to finish): ")
        if data == "":
            break
        exam_points, exercise_points = data.split()
        exams.append(int(exam_points))
        exercises.append(int(exercise_points))
        
    exam_pass = exam_fail(exams)
    totals = total_points(exams, exercises)
    grades = grade(totals, exam_pass)
    passed = pass_percentage(grades)
    avg = mean(totals)
    printing(avg, passed)
    grade_distribution(grades)

def printing(avg, passing):
    print("Statistics:")
    print(f"Points average: {avg:.1f}")
    print(f"Pass percentage: {passing:.1f}")

def exam_fail(exams):
    new = []
    for point in exams:
        if point < 10:
            new.append(False)
        else:
            new.append(True)
    return new

def total_points(exams, exercises):
    new = []
    for i in range(len(exercises)):
        total = exercises[i] // 10 + exams[i]
        new.append(total)
    return new

def grade(totals, exam_pass):
    grades = []
    for i in range(len(totals)):
        if not exam_pass[i]:
            grades.append(0)
        else:
            if totals[i] >= 0 and totals[i] <= 14:
                grades.append(0)
            elif totals[i] >= 15 and totals[i] <= 17:
                grades.append(1)
            elif totals[i] >= 18 and totals[i] <= 20:
                grades.append(2)
            elif totals[i] >= 21 and totals[i] <= 23:
                grades.append(3)
            elif totals[i] >= 24 and totals[i] <= 27:
                grades.append(4)
            elif totals[i] >= 28 and totals[i] <= 30:
                grades.append(5)
    return grades

def mean(totals):
    if not totals:
        return 0
    total_sum = sum(totals)
    return total_sum / len(totals)

def pass_percentage(grades):
    count_passing = sum(1 for grade in grades if grade > 0)
    return (count_passing / len(grades)) * 100

def grade_distribution(grades):
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = grades.count(i)
        print(f"{i}: {'*' * stars}")


grade_input()