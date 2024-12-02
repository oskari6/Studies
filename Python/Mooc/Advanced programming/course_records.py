class Course:
    def __init__(self, name, grade, credits):
        self.name = name
        self.grade = int(grade)
        self.credits = int(credits)
    def __str__(self):
        return f"{self.name} ({self.credits} cr) grade {self.grade}"
    
class Studies:
    def __init__(self):
        self.courses = {}

    def add_course(self, course):
        if course.name not in self.courses:
            self.courses[course.name] = course
        else:
            if course.grade > self.courses[course.name].grade:
                self.courses[course.name].grade = course.grade

    def get_course(self, name):
        if name not in self.courses:
            return "no entry for this course"
        return self.courses[name]
    
    def mean(self):
        if not self.courses:
            return 0
        total = sum(course.grade for course in self.courses.values())
        return total / len(self.courses)
    
    def completed(self):
        return len(self.courses)
    
    def distribution(self):
        distribution = {1: "", 2: "", 3: "", 4: "", 5: ""}
        for course in self.courses.values():
            distribution[course.grade] += "x"
        for grade in range(1, 6):
            print(f"{grade}: {distribution[grade]}")

    def credits(self):
        return sum(course.credits for course in self.courses.values())
    
class StudyApp:
    def __init__(self):
        self.courses = Studies()
        
    def add_course(self):
        name = input("course:")
        grade = input("grade:")
        credits = input("credits:")
        course = Course(name, grade, credits)
        self.courses.add_course(course)

    def get_course(self):
        name = input("course:")
        course= self.courses.get_course(name)
        print(course)

    def stats(self):
        completed = self.courses.completed()
        credits = self.courses.credits()
        mean = self.courses.mean()
        print(f"{completed} completed courses, a total of {credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        self.courses.distribution()

    def printing(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def execute(self):
        self.printing()
        while True:
            command = int(input("command:"))
            if command == 0:
                break
            elif command == 1:
                self.add_course()
            elif command == 2:
                self.get_course()
            elif command == 3:
                self.stats()
            else:
                self.printing()

app = StudyApp()
app.execute()