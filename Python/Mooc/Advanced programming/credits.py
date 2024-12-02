from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(attempts):
    return reduce(lambda total, sum: total + sum.credits, attempts, 0)

def sum_of_passed_credits(attempts):
    courses = filter(lambda course:course.grade >= 1, attempts)
    return reduce(lambda total, sum: total + sum.credits, courses, 0)

def average(attempts):
    courses = list(filter(lambda course:course.grade >= 1, attempts))
    total = reduce(lambda total, sum: total + sum.grade, courses, 0)
    return  total / len(courses)

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)